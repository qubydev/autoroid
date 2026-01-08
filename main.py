from langchain_core.messages import HumanMessage
from app.config import RECURSION_LIMIT
from app.logger import Colors, clean_output
from app.adb import is_device_connected
from app.agent import get_agent_graph

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    if not is_device_connected():
        print(f"{Colors.FAIL}❌ No ADB devices found.{Colors.ENDC}")
        exit(1)

    print(f"{Colors.HEADER}🤖 Android Agent Started{Colors.ENDC}")
    goal = input(f"{Colors.BOLD}Enter Goal: {Colors.ENDC}")
    
    agent = get_agent_graph()
    messages = [HumanMessage(content=goal)]
    
    for chunk in agent.stream({"messages": messages}, {"recursion_limit": RECURSION_LIMIT}, stream_mode="updates"):
        
        # 1. LLM Decisions
        if "llm_call" in chunk:
            msg = chunk["llm_call"]["messages"][-1]
            if msg.content:
                print(f"\n{Colors.CYAN}🧠 THINKING:{Colors.ENDC}\n   {msg.content}")
            if msg.tool_calls:
                for tc in msg.tool_calls:
                    print(f"\n{Colors.BLUE}👉 ACTION: {Colors.BOLD}{tc['name']}{Colors.ENDC} {tc['args']}")

        # 2. Tool Results
        elif "tool_node" in chunk:
            for msg in chunk["tool_node"]["messages"]:
                content = clean_output(msg.content)
                print(f"\n{Colors.GREEN}👀 OBSERVATION:{Colors.ENDC}\n   {content}")

    print(f"\n{Colors.HEADER}✅ Done!{Colors.ENDC}")
