from pydantic import BaseModel
from uuid import UUID

class ChatRequest(BaseModel):
    message: str
    thread_id: UUID | None = None

class ChatResponse(BaseModel):
    reply: str
    thread_id: UUID