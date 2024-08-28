from sqlalchemy import CheckConstraint

from .base import *


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int]
    username: Mapped[str] = mapped_column(index=True, unique=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    name: Mapped[str | None]
    gender: Mapped[str | None] = mapped_column(String(1, collation='NOCASE'), CheckConstraint("gender in ('м', 'ж')"))
    age: Mapped[int | None] = mapped_column(CheckConstraint("age >= 5 and age <= 150"))
