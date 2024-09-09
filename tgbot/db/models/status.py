from sqlalchemy import Index, CheckConstraint
from sqlalchemy.orm import relationship

from .base import *


class Status(Base):
    __tablename__ = "statuses"

    status_text: Mapped[str | None]
    grade: Mapped[int | None] = mapped_column(CheckConstraint("grade >= -5 and grade <= 5"))
    user_id: Mapped[userfk]

    __table_args__ = (
        Index("status_user_id_created_at_index", "user_id", "created_at", unique=True),
    )

    user: Mapped["User"] = relationship(
        back_populates="statuses"
    )

    def __repr__(self):
        return (f"id={self.id} "
                f"user_id={self.user_id} "
                f"text={self.status_text} "
                f"grade={self.grade} "
                f"created_at={self.created_at} "
                f"updated_at={self.updated_at}")

    def __eq__(self, __value):
        first = (self.id, self.status_text, self.grade, self.user_id)
        second = (__value.user_id, __value.status_text, __value.grade)
        return first == second

    def __hash__(self):
        hash((self.id, self.status_text, self.grade, self.user_id, self.created_at, self.updated_at))
