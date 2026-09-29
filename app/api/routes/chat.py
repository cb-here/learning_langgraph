from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.dependencies.chat import get_chatbot
from app.services import chat_service

router = APIRouter(tags=["Chat"])

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, chatbot=Depends(get_chatbot)):
    try:
        response = await chat_service.send_message(chatbot=chatbot, message=request.message, thread_id=request.thread_id)

        return response 

    except chat_service.ThreadNotFound:
        raise HTTPException(
            status_code=404, 
            detail="Thread not found"
        )