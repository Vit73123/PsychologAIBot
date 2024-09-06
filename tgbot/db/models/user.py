import enum

from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

from .base import *


class Gender(enum.Enum):
    male = 1
    female = 2


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(index=True, unique=True)
    username: Mapped[str]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    name: Mapped[str | None]
    gender: Mapped[Gender | None]
    age: Mapped[int | None] = mapped_column(CheckConstraint("age >= 5 and age <= 150"))

    statuses: Mapped[list["Status"]] = relationship(
        back_populates="user",
        order_by="Status.updated_at.desc()",
        cascade='save-update, merge, delete'
    )

    appointments: Mapped[list["Appointment"]] = relationship(
        back_populates="user",
        order_by="Appointment.updated_at.desc()",
        cascade='save-update, merge, delete'
    )

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
        first = (self.username, self.first_name, self.last_name)
        second = (__value.username, __value.first_name, __value.last_name)
        return first == second

    def __hash__(self):
        hash((self.id, self.created_at, self.updated_at, self.user_id, self.username, self.first_name, self.last_name))
