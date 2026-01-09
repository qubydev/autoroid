from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import LLM_PROVIDER, BASE_URL, API_KEY, MODEL

def get_model():
    if LLM_PROVIDER == "openai":
        return ChatOpenAI(
            base_url=BASE_URL if BASE_URL else None,
            api_key=API_KEY,
            model=MODEL,
        )
    elif LLM_PROVIDER == "anthropic":
        return ChatAnthropic(
            base_url=BASE_URL if BASE_URL else None,
            api_key=API_KEY,
            model=MODEL,
        )
    elif LLM_PROVIDER == "gemini":
        return ChatGoogleGenerativeAI(
            model=MODEL,
            google_api_key=API_KEY,
            # Strict mode
            convert_system_message_to_human=False 
        )
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
