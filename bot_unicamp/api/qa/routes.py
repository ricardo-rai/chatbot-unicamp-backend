from fastapi import APIRouter

from config import settings

from bot_unicamp.history import (
    History,
    HistoryController,
    HistoryService,
    HistoryRepository,
)
from bot_unicamp.bot import BotController, BotService, BotRepository
from bot_unicamp.drivers import MongoDatabaseContext


def setup(nn):
    router = APIRouter()

    @router.post("/bot", tags=["get answer for a question"])
    def post_question_answer(episode: History):

        bot_repository = BotRepository()
        mongodb_bot = MongoDatabaseContext(
            db_uri=settings.get("MONGODB_DSN"),
            db_name="BotUnicamp",
            db_collection="contexts",
        )
        bot_service = BotService(
            bot_repository=bot_repository,
            create_database_context=mongodb_bot,
        )
        bot_controller = BotController(
            bot_service=bot_service,
        )

        episode = bot_controller.ask(episode, nn)

        history_repository = HistoryRepository()
        mongodb_history = MongoDatabaseContext(
            db_uri=settings.get("MONGODB_DSN"),
            db_name="BotUnicamp",
            db_collection="history",
        )
        history_service = HistoryService(
            history_repository=history_repository,
            create_database_context=mongodb_history,
        )
        history_controller = HistoryController(
            history_service=history_service,
        )

        response = history_controller.add(episode)

        return response

    return router
