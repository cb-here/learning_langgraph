from app.agents.chat import ChatState, SYSTEM_PROMPT
from app.llm import get_llm
from langchain_core.messages import SystemMessage

async def chat_node(state: ChatState) -> dict:
    llm = get_llm()

    messages = [SystemMessage(content=SYSTEM_PROMPT), *state["messages"]]

    response = await llm.ainvoke(messages)

    return {
        "messages": [response]
    }