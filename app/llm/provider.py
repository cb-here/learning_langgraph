from langchain_openai import ChatOpenAI
from app.core import settings

def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        api_key=settings.openai_api_key,
        model=settings.chat_model_name,
        temperature=0
    )