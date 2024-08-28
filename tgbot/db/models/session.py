from sqlalchemy import Index

from .base import *


class Session(Base):
    __tablename__ = "sessions"

    review: Mapped[str | None]
    user_id: Mapped[userfk]

    __table_args__ = (
        Index("sessions_created_at_user_id_index", "created_at", "user_id", unique=True),
    )
