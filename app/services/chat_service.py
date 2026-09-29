from langchain_core.messages import HumanMessage
from uuid import UUID, uuid4
from app.utils import generate_runnable_config
import logging

logger = logging.getLogger(__name__)

class ThreadNotFound(Exception):
    """Raise when thread not found."""

async def send_message(chatbot, message: str, thread_id: UUID | None = None) -> dict:
    if thread_id is None:
        thread_id = uuid4()
    else:
        snapshot = await chatbot.aget_state(generate_runnable_config(str(thread_id)))
        if not snapshot.values:
            raise ThreadNotFound()


    config = generate_runnable_config(str(thread_id))

    response = await chatbot.ainvoke({
        "messages": [HumanMessage(content=message)]
    }, config=config)

    return {
        "reply": response["messages"][-1].content, 
        "thread_id": thread_id
    }
