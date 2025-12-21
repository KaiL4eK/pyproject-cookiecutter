"""Database entities logic."""
from uv_project_ty_ruff_bitbucket_streamlit.db.sync.repositories.user import UserRepository
from uv_project_ty_ruff_bitbucket_streamlit.db.sync.engine import db_session
from uv_project_ty_ruff_bitbucket_streamlit.schemas.user import (
    UserFilterModel,
    UserCreateModel,
    UserBase,
)


@db_session
def add_new_user(user: UserCreateModel, session):
    """Add new user to DB."""
    user_dao = UserRepository(session)
    user_dao.add(user)


@db_session
def get_all_users(session) -> list[UserBase]:
    """Get all users from DB."""
    user_dao = UserRepository(session)
    user_entities = user_dao.find_all()

    return [UserBase.model_validate(user_entity) for user_entity in user_entities]


@db_session
def find_user_by_username(username: str, session) -> UserBase:
    """Find user by username from DB."""
    user_dao = UserRepository(session)
    user_entity = user_dao.find_one_or_none(
        filters=UserFilterModel(username=username)
    )

    if not user_entity:
        return None

    return UserBase.model_validate(user_entity)
