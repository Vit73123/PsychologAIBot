from sqlalchemy import Index, CheckConstraint

from .base import *


class Status(Base):
    __tablename__ = "statuses"

    text: Mapped[str | None]
    grade: Mapped[int] = mapped_column(CheckConstraint("grade >= -5 and grade <= 5"))
    user_id: Mapped[userfk]

    __table_args__ = (
        Index("status_created_at_user_id_index", "created_at", "user_id", unique=True),
    )

    def __eq__(self, __value):
        first = (self.text, self.grade, self.user_id)
        second = (__value.text, __value.grade, __value.user_id)
        return first == second

    def __hash__(self):
        hash((self.id, self.created_at, self.updated_at, self.text, self.grade, self.user_id))
