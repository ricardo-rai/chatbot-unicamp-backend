from .models import History
from .service import HistoryService

from bot_unicamp.common import GenericError


class HistoryController:
    def __init__(
        self,
        history_service: HistoryService,
    ):
        self.history_service = history_service

    def add(self, episode: History) -> History:
        try:
            history = self.history_service.add(episode)
        except Exception as err:
            raise GenericError(err)

        return history
