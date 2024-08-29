from tgbot.config.config import DBConfig
from tgbot.db.models.base import Base
from .base import BaseRepo
from .session import SessionRepo
from .status import StatusRepo
from .user import UserRepo


class Repo(BaseRepo):
    user: UserRepo
    session: SessionRepo
    status: StatusRepo

    def __init__(self, db_config: DBConfig):
        super().__init__(db_config)
        self.user = UserRepo(self.pool)
        self.session = SessionRepo(self.pool)
        self.status = StatusRepo(self.pool)

    async def create_tables(self):
        async with self.engine.begin() as conn:
            self.engine.echo = False
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            self.engine.echo = self.db_config.is_echo
