from typing import Optional
from pydantic import BaseModel


class History(BaseModel):
    askedAt: Optional[str]
    answeredAt: Optional[str]
    context: Optional[str]
    question: str
    answer: Optional[str]
