from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AnyMessage, SystemMessage, ToolMessage
from typing_extensions import TypedDict, Annotated
import operator
import time
from typing import Literal

from app.llm import get_model
from app.tools import tools, tools_by_name
from app.prompts import SYSTEM_PROMPT
from app.config import RATE_LIMIT_DELAY

# Initialize model and bind tools
model = get_model()
model_with_tools = model.bind_tools(tools)

class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

def llm_call(state: dict):
    time.sleep(RATE_LIMIT_DELAY) # Rate limit safety
    return {
        "messages": [
            model_with_tools.invoke(
                [
                    SystemMessage(content=SYSTEM_PROMPT)
                ] 
                + state["messages"]
            )
        ],
    }

def tool_node(state: dict):
    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=str(observation), tool_call_id=tool_call["id"]))
    return {"messages": result}

def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    last_message = state["messages"][-1]
    return "tool_node" if last_message.tool_calls else END

def get_agent_graph():
    # Build Graph
    agent_builder = StateGraph(MessagesState)
    agent_builder.add_node("llm_call", llm_call)
    agent_builder.add_node("tool_node", tool_node)
    agent_builder.add_edge(START, "llm_call")
    agent_builder.add_conditional_edges("llm_call", should_continue, ["tool_node", END])
    agent_builder.add_edge("tool_node", "llm_call")
    return agent_builder.compile()
