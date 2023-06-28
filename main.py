from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from transformers import pipeline

from bot_unicamp.api.router import setup_router
from bot_unicamp.common import Logger
from config import settings


def app() -> FastAPI:
    model_name = settings.MODEL_NAME

    nn = pipeline("question-answering", model=model_name)

    app = FastAPI(title=settings.PROJECT_NAME)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(setup_router(nn), prefix=settings.API_PREFIX)

    return app


Logger.setup_logging()

app()
