from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    userId: int = Field(None, example=000000)
    point: int = Field(None, example=000000)
    exchange: dict = Field(None)
    histories: list = Field(None)
class History(BaseModel):
    clubId: int
    description: str
    dateTime: str
    point: int