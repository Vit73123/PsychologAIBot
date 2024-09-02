from sqlalchemy import Index, CheckConstraint
from sqlalchemy.orm import relationship

from .base import *


class Status(Base):
    __tablename__ = "statuses"

    text: Mapped[str | None]
    grade: Mapped[int] = mapped_column(CheckConstraint("grade >= -5 and grade <= 5"))
    user_id: Mapped[userfk]

    __table_args__ = (
        Index("status_created_at_user_id_index", "created_at", "user_id", unique=True),
    )

    user: Mapped["User"] = relationship(
        back_populates="statuses"
    )

    def __repr__(self):
        return (f"{self.id=} "
                f"{self.user_id=} "
                f"{self.text=} "
                f"{self.grade=} "
                f"{self.created_at=} "
                f"{self.updated_at=}")

    def __eq__(self, __value):
        first = (self.id, self.text, self.grade, self.user_id)
        second = (__value.user_id, __value.text, __value.grade)
        return first == second

    def __hash__(self):
        hash((self.id, self.text, self.grade, self.user_id, self.created_at, self.updated_at))
