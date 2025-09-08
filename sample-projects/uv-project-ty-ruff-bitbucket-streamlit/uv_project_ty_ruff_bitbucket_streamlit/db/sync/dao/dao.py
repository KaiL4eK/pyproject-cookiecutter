from uv_project_ty_ruff_bitbucket_streamlit.db.models import User

from .base import BaseDAO


class UserDAO(BaseDAO):
    model = User
