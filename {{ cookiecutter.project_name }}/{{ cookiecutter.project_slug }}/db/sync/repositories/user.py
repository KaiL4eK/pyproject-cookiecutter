from {{cookiecutter.project_slug}}.db.models import User
from {{cookiecutter.project_slug}}.schemas.user import UserBase

from .base import BaseRepository


class UserRepository(BaseRepository[User, UserBase]):
    model = User
    schema_class = UserBase
