from datetime import datetime
from typing import Annotated

from sqlalchemy import ForeignKey, text
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]
userfk = Annotated[int, mapped_column(ForeignKey("users.id", ondelete='CASCADE'))]
date_time_now = Annotated[datetime, mapped_column(server_default=text("(DATETIME('now'))"))]  # date time in UTC
date_time_now_upd = Annotated[datetime, mapped_column(server_default=text("(DATETIME('now'))"),
                                                      onupdate=text("(DATETIME('now'))"))]  # date time in UTC

str_256 = Annotated[str, 'nocase']


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }

    id: Mapped[intpk]
    created_at: Mapped[date_time_now]
    updated_at: Mapped[date_time_now_upd]

