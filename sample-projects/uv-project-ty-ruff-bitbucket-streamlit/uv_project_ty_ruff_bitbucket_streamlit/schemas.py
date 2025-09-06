from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

OptionalStr = Annotated[str | None, Field(default=None)]
OptionalInt = Annotated[int | None, Field(default=None)]
OptionalFloat = Annotated[float | None, Field(default=None)]
OptionalDatetime = Annotated[datetime | None, Field(default=None)]


class BaseORMModel(BaseModel):
    """Base class to bound add, update, retrieve operations to ORM models."""

    class Config:
        from_attributes = True


class BaseORMFilterModel(BaseModel):
    """Base class to bound filtering operations to ORM models."""


class UserModel(BaseORMModel):
    id: OptionalInt
    username: str
    age: int
    added_at: OptionalDatetime


class UserFilterModel(BaseORMModel):
    username: str
