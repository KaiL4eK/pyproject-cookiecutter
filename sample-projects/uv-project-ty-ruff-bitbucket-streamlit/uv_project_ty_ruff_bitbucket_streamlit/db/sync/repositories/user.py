from uv_project_ty_ruff_bitbucket_streamlit.db.models import User
from uv_project_ty_ruff_bitbucket_streamlit.schemas.user import UserBase

from .base import BaseRepository


class UserRepository(BaseRepository[User, UserBase]):
    model = User
    schema_class = UserBase
