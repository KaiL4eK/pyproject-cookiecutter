"""Database entities logic."""
from {{cookiecutter.project_slug}}.db.sync.dao.dao import UserDAO
from {{cookiecutter.project_slug}}.db.sync.engine import session_commited
from {{cookiecutter.project_slug}}.schemas import (
    UserFilterModel,
    UserModel,
)


@session_commited
def add_new_user(user: UserModel, session):
    """Add new user to DB."""
    user_dao = UserDAO(session)
    user_dao.add(user)


@session_commited
def get_all_users(session) -> list[UserModel]:
    """Get all users from DB."""
    user_dao = UserDAO(session)
    user_entities = user_dao.find_all()

    return [UserModel.model_validate(user_entity) for user_entity in user_entities]


@session_commited
def find_user_by_username(username: str, session) -> UserModel:
    """Find user by username from DB."""
    user_dao = UserDAO(session)
    user_entity = user_dao.find_one_or_none(filters=UserFilterModel(username=username))

    if not user_entity:
        return None

    return UserModel.model_validate(user_entity)
