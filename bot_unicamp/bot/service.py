from datetime import datetime as dt
from typing import List
from transformers import pipeline

from .models import Context
from .repository import BotRepository

from bot_unicamp.drivers import MongoDatabaseContext
from bot_unicamp.history import History


class BotService:
    def __init__(
        self,
        bot_repository: BotRepository,
        create_database_context: MongoDatabaseContext,
    ):
        self.bot_repository = bot_repository
        self.create_database_context = create_database_context

    def _get_answer(
        self, episode: History, contexts: List[Context], nn: pipeline
    ) -> History:

        answer = {"score": 0}
        for context in contexts:
            result = nn(question=episode.question, context=context.context)
            if result["score"] > answer["score"]:
                answer = result
                episode.context = context.context
                episode.answer = result["answer"]

        return episode

    def _get_contexts(
        self,
    ) -> List[Context]:
        with self.create_database_context as db:
            contexts = self.bot_repository.get_all(db)

        return contexts

    def ask(self, episode: History, nn: pipeline) -> History:
        episode.askedAt = str(dt.now())
        contexts = self._get_contexts()

        return self._get_answer(episode, contexts, nn)
