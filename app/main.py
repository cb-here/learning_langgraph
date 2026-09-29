from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core import setup_logging
from app.api import api_router
from app.agents.chat import build_graph
from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from app.core import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with AsyncConnectionPool(
            conninfo=settings.database_url.get_secret_value(),
            max_size=10,
            open=False,
            kwargs={
                "autocommit": True, 
                "prepare_threshold": 0,
                "row_factory": dict_row
            }
        ) as pool:
            checkpointer = AsyncPostgresSaver(pool)
            await checkpointer.setup()
            app.state.chatbot = build_graph(checkpointer=checkpointer)
            yield
    finally:
         pass

def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(
        title="Chatbot",
        version="1.0.0",
        lifespan=lifespan
    )

    app.include_router(router=api_router)

    return app

app = create_app()