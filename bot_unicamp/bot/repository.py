from typing import List

from .models import Context

from bot_unicamp.drivers import MongoDatabaseContext


class BotRepository:
    def get_all(self, db: MongoDatabaseContext) -> List[Context]:
        return [Context.parse_obj(value) for value in db.get_all()]
