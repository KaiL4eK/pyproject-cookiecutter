import uuid
from datetime import datetime
from decimal import Decimal
from typing import Annotated

from sqlalchemy import (
    create_engine,
    inspect,
)
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, sessionmaker

from {{cookiecutter.project_slug}}.settings import DatabaseSettings

db_settings = DatabaseSettings()


engine = create_engine(db_settings.sqlalchemy_uri_sync, echo=db_settings.echo, pool_pre_ping=True)
session_maker = sessionmaker(engine, expire_on_commit=False)
# Just type to set unique
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

    def to_dict(self, exclude_none: bool = False):
        """
        Converts the model object to a dictionary.

        Args:
            exclude_none (bool): Whether to exclude None values from the result

        Returns:
            dict: Dictionary with object data
        """
        result = {}
        for column in inspect(self.__class__).columns:
            value = getattr(self, column.key)

            # Convert special data types
            if isinstance(value, datetime):
                value = value.isoformat()
            elif isinstance(value, Decimal):
                value = float(value)
            elif isinstance(value, uuid.UUID):
                value = str(value)

            # Add value to result
            if not exclude_none or value is not None:
                result[column.key] = value

        return result

    def __repr__(self) -> str:
        """String representation of the object for debugging purposes."""
        return f"<{self.__class__.__name__}>"


def session_commited(method):
    """Wrapper"""

    def wrapper(*args, **kwargs):
        with session_maker() as session:
            with session.begin():
                return method(*args, session=session, **kwargs)

    return wrapper
