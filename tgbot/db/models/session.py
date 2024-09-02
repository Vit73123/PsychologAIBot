from sqlalchemy import Index
from sqlalchemy.orm import relationship

from .base import *


class Session(Base):
    __tablename__ = "sessions"

    review: Mapped[str | None]
    user_id: Mapped[userfk]

    __table_args__ = (
        Index("sessions_created_at_user_id_index", "created_at", "user_id", unique=True),
    )

    user: Mapped["User"] = relationship(
        back_populates="sessions"
    )

    def __repr__(self):
        return (f"{self.id=} "
                f"{self.user_id=} "
                f"{self.review=} "
                f"{self.created_at=} "
                f"{self.updated_at=}")

    def __eq__(self, __value):
        first = (self.review, self.user_id)
        second = (__value.review, __value.user_id)
        return first == second

    def __hash__(self):
        hash((self.id, self.created_at, self.updated_at, self.review, self.user_id))
