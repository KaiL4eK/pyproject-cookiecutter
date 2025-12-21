import uuid
from decimal import Decimal
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr

# ---------- SQLAlchemy 2.0 Base ----------

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:  # noqa: N805
        return cls.__name__.lower() + "s"

    def to_dict(self, exclude_none: bool = False):
        """
        Converts the model object to a dictionary.

        Parameters
        ----------
        exclude_none : bool
            Whether to exclude None values from the result

        Returns
        -------
        dict
            Dictionary with object data
        """
        result = {}
        for column in sa.inspect(self.__class__).columns:
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

# ---------- Tables ----------

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        sa.Integer,
        primary_key=True,
    )

    username: Mapped[str | None] = mapped_column(sa.String, nullable=False, unique=True)
    age: Mapped[int | None] = mapped_column(sa.Integer, nullable=False)
    added_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True), server_default=sa.func.now()
    )
