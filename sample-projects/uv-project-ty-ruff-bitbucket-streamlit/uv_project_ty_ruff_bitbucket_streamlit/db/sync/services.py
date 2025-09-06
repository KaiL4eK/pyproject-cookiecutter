from uv_project_ty_ruff_bitbucket_streamlit.db.sync.dao.dao import UserDAO
from uv_project_ty_ruff_bitbucket_streamlit.db.sync.engine import session_commited
from uv_project_ty_ruff_bitbucket_streamlit.schemas import (
    UserFilterModel,
    UserModel,
)


@session_commited
def add_new_user(user: UserModel, session):
    user_dao = UserDAO(session)
    user_dao.add(user)


@session_commited
def get_all_users(session) -> list[UserModel]:
    user_dao = UserDAO(session)
    user_entities = user_dao.find_all()

    return [UserModel.model_validate(user_entity) for user_entity in user_entities]


@session_commited
def find_user_by_username(username: str, session) -> UserModel:
    user_dao = UserDAO(session)
    user_entity = user_dao.find_one_or_none(filters=UserFilterModel(username=username))

    if not user_entity:
        return None

    return UserModel.model_validate(user_entity)
