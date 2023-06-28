from pydantic import BaseModel


class Context(BaseModel):
    subject: str
    context: str
