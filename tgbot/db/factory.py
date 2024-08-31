from logging import getLogger

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)
from sqlalchemy.ext.asyncio import create_async_engine

from tgbot.config.config import DBConfig
from tgbot.tools.logger import get_logger_dev
from .models.base import Base
from .repo import Repo

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def create_pool(db_config: DBConfig) -> async_sessionmaker[AsyncSession]:
    engine = create_engine(db_config)
    return create_session_maker(engine)


def create_engine(db_config: DBConfig) -> AsyncEngine:
    return create_async_engine(url=db_config.dsn, echo=db_config.is_echo)


def create_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    pool: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine, expire_on_commit=False, autoflush=False
    )
    return pool


def create_repo(engine: AsyncEngine):
    log.debug(" create repo...")
    pool = create_session_maker(engine)
    return Repo(pool)


async def create_tables(engine: AsyncEngine, db_config: DBConfig):
    log.debug(" create tables...")
    async with engine.begin() as conn:
        engine.echo = False
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        engine.echo = db_config.is_echo
