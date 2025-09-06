from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

# ---------- SQLAlchemy 2.0 Base ----------
from {{cookiecutter.project_slug}}.db.sync.engine import Base

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
