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
