from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
    AsyncEngine
)

from tgbot.config.config import DBConfig
from tgbot.db.models.base import Base
from .session import SessionRepo
from .status import StatusRepo
from .user import UserRepo


class DbRepo:
    user_repo: UserRepo
    session_repo: SessionRepo
    status_repo: StatusRepo

    engine: AsyncEngine
    pool: async_sessionmaker[AsyncSession]
    db_config: DBConfig

    def __init__(self, db_config: DBConfig):
        self.db_config = db_config
        self.engine = create_async_engine(
            url=db_config.dsn,
            echo=db_config.is_echo
        )
        self.pool: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

        self.user_repo = UserRepo(self.pool)
        self.session_repo = SessionRepo(self.pool)
        self.status_repo = StatusRepo(self.pool)

    async def create_tables(self):
        async with self.engine.begin() as conn:
            self.engine.echo = False
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            self.engine.echo = self.db_config.is_echo
