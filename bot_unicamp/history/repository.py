from .models import History

from bot_unicamp.drivers import MongoDatabaseContext


class HistoryRepository:
    def add(self, db: MongoDatabaseContext, value: History) -> History:
        return History.parse_obj(db.add(value.dict()))
