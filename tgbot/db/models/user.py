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

    def f(self):
        a = super().id

    def __repr__(self):
        return (f"id={self.id} "
                f"user_id={self.user_id} "
                f"username={self.username} "
                f"first_name={self.first_name} "
                f"last_name={self.last_name} "
                f"name={self.name} "
                f"gender={self.gender} "
                f"age={self.age} "
                f"created_at={self.created_at} "
                f"updated_at={self.updated_at}")

    def __eq__(self, __value):
        first = (self.user_id, self.username, self.first_name, self.last_name)
        second = (__value.user_id, __value.username, __value.first_name, __value.last_name)
        return first == second

    def __hash__(self):
        hash((self.id, self.created_at, self.updated_at, self.user_id, self.username, self.first_name, self.last_name))
