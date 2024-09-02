from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

from .base import *


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(index=True, unique=True)
    username: Mapped[str]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    name: Mapped[str | None]
    gender: Mapped[str | None] = mapped_column(String(1, collation='NOCASE'), CheckConstraint("gender in ('м', 'ж')"))
    age: Mapped[int | None] = mapped_column(CheckConstraint("age >= 5 and age <= 150"))

    statuses: Mapped[list["Status"]] = relationship(
        back_populates="user",
        order_by="Status.updated_at.desc()",
        cascade='save-update, merge, delete'
    )

    sessions: Mapped[list["Session"]] = relationship(
        back_populates="user",
        order_by="Session.updated_at.desc()",
        cascade='save-update, merge, delete'
    )

    def __repr__(self):
        return (f"{self.id=} "
                f"{self.user_id=} "
                f"{self.username=} "
                f"{self.first_name=} "
                f"{self.last_name=} "
                f"{self.name=} "
                f"{self.gender=} "
                f"{self.age=} "
                f"{self.created_at=} "
                f"{self.updated_at=}")

    def __eq__(self, __value):
        first = (self.username, self.first_name, self.last_name)
        second = (__value.username, __value.first_name, __value.last_name)
        return first == second

    def __hash__(self):
        hash((self.id, self.created_at, self.updated_at, self.user_id, self.username, self.first_name, self.last_name))
