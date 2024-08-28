import enum
from datetime import datetime
from typing import Annotated

from sqlalchemy import String, text, CheckConstraint, Index, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

intpk = Annotated[int, mapped_column(primary_key=True)]
userfk = Annotated[int, mapped_column(ForeignKey("users.id", ondelete='CASCADE'))]
date_time_now = Annotated[datetime, mapped_column(server_default=text("(DATETIME('now'))"))]  # date time in UTC

str_256 = Annotated[str, 'nocase']


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }


class Gender(enum.Enum):
    male = "м"
    female = "ж"


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    user_id: Mapped[int]
    username: Mapped[str] = mapped_column(index=True, unique=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    name: Mapped[str | None]
    gender: Mapped[str | None] = mapped_column(String(1, collation='NOCASE'), CheckConstraint("gender in ('м', 'ж')"))
    age: Mapped[int | None] = mapped_column(CheckConstraint("age >= 5 and age <= 150"))
    created_at: Mapped[date_time_now]
    updated_at: Mapped[date_time_now]


class Status(Base):
    __tablename__ = "statuses"

    id: Mapped[intpk]
    text: Mapped[str | None]
    grade: Mapped[int] = mapped_column(CheckConstraint("grade >= -5 and grade <= 5"))
    created_at: Mapped[date_time_now]
    user_id: Mapped[userfk]

    __table_args__ = (
        Index("status_created_at_user_id_index", "created_at", "user_id", unique=True),
    )


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[intpk]
    review: Mapped[str | None]
    created_at: Mapped[date_time_now]
    user_id: Mapped[userfk]

    __table_args__ = (
        Index("sessions_created_at_user_id_index", "created_at", "user_id", unique=True),
    )
