from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
    AsyncEngine
)

from tgbot.config.config import DBConfig


class BaseRepo:
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
