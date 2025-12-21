from datetime import datetime

from uv_project_ty_ruff_bitbucket_streamlit.schemas.base import (
    BaseORMFilterModel,
    BaseORMModel,
    BaseORMCreateModel
)


class UserBase(BaseORMModel):
    """User object model."""

    id: int
    username: str
    age: int
    added_at: datetime | None = None


class UserCreateModel(BaseORMCreateModel):
    """User creation model."""
    username: str
    age: int


class UserFilterModel(BaseORMFilterModel):
    """User filtering model."""

    username: str | None = None
