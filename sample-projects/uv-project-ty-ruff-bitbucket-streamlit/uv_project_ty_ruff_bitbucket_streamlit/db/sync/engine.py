from typing import Annotated

from sqlalchemy import create_engine
from sqlalchemy.orm import mapped_column, sessionmaker

from uv_project_ty_ruff_bitbucket_streamlit.settings.db import DatabaseSettings

db_settings = DatabaseSettings()


engine = create_engine(
    db_settings.sqlalchemy_uri_sync,
    echo=db_settings.echo,
    pool_pre_ping=True
)
session_maker = sessionmaker(engine, expire_on_commit=False)
# Just type to set unique
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]


def db_session(method):
    """Wrapper for services providing session object."""

    def wrapper(*args, **kwargs):
        with session_maker.begin() as session:
            return method(*args, session=session, **kwargs)

    return wrapper
