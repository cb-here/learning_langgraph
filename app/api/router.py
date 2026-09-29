from fastapi import APIRouter
from app.api.routes import health_router, chat_router

api_router = APIRouter(prefix="/api")

api_router.include_router(router=health_router)

api_router.include_router(prefix="/chat", router=chat_router)
