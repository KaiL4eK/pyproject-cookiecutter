from {{cookiecutter.project_slug}}.db.models import User

from .base import BaseDAO


class UserDAO(BaseDAO):
    model = User
