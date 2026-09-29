from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/")
async def root():
    return {
        "message": "Welcome to my chatbot"
    }

@router.get("/status")
async def status():
    return {
        "message": "Server is healthy and running..."
    }