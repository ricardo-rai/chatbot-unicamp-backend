from fastapi import APIRouter

from bot_unicamp.api import qa


def setup_router(nn):
    router = APIRouter()
    router.include_router(qa.setup(nn), prefix="/qa")

    return router
