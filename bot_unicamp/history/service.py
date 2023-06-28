from datetime import datetime as dt

from .models import History
from .repository import HistoryRepository

from bot_unicamp.drivers import MongoDatabaseContext


class HistoryService:
    def __init__(
        self,
        history_repository: HistoryRepository,
        create_database_context: MongoDatabaseContext,
    ):
        self.history_repository = history_repository
        self.create_database_context = create_database_context

    def add(self, episode: History) -> History:
        episode.answeredAt = str(dt.now())
        with self.create_database_context as db:
            return self.history_repository.add(db, episode)
