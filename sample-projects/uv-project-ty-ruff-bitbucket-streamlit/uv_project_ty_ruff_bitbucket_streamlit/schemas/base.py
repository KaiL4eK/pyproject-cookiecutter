"""Models to mirror ORM representations in more general way."""
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict

OptionalStr = Annotated[str | None, Field(default=None)]
OptionalInt = Annotated[int | None, Field(default=None)]
OptionalFloat = Annotated[float | None, Field(default=None)]
OptionalDatetime = Annotated[datetime | None, Field(default=None)]


class BaseORMModel(BaseModel):
    """Base class to represent ORM models from DB."""

    model_config = ConfigDict(from_attributes=True)


class BaseORMCreateModel(BaseModel):
    """Base class to bound creation operations to ORM models."""

    model_config = ConfigDict(extra="forbid")


class BaseORMFilterModel(BaseModel):
    """Base class to bound filtering operations to ORM models."""

    model_config = ConfigDict(extra="forbid")


class BaseORMUpdateModel(BaseModel):
    """Base class to bound update operations to ORM models."""

    model_config = ConfigDict(extra="forbid")
