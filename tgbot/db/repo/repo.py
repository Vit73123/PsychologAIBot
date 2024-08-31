from sqlalchemy.ext.asyncio import (
    async_sessionmaker
)

from .session_repo import SessionRepo
from .status_repo import StatusRepo
from .user_repo import UserRepo


class Repo:
    user: UserRepo
    session: SessionRepo
    status: StatusRepo

    pool: async_sessionmaker

    def __init__(self, pool: async_sessionmaker):
        self.pool = pool

        self.user = UserRepo(self.pool)
        self.session = SessionRepo(self.pool)
        self.status = StatusRepo(self.pool)
