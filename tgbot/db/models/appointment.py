from sqlalchemy import Index
from sqlalchemy.orm import relationship

from .base import *


class Appointment(Base):
    __tablename__ = "appointments"

    review: Mapped[str | None]
    user_id: Mapped[userfk]

    __table_args__ = (
        Index("appointments_user_id_created_at_index", "user_id", "created_at", unique=True),
    )

    user: Mapped["User"] = relationship(
        back_populates="appointments"
    )

    def __repr__(self):
        return (f"id={self.id} "
                f"user_id={self.user_id} "
                f"review={self.review} "
                f"created_at={self.created_at} "
                f"updated_at={self.updated_at}")

    def __eq__(self, __value):
        first = (self.review, self.user_id)
        second = (__value.review, __value.user_id)
        return first == second

    def __hash__(self):
        hash((self.id, self.created_at, self.updated_at, self.review, self.user_id))
