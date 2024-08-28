from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
    AsyncEngine
)

from tgbot.config.config import DBConfig
from tgbot.db.models import Base


def create_pool(db_config: DBConfig) -> async_sessionmaker[AsyncSession]:
    engine = create_engine(db_config)
    return create_session_maker(engine)


def create_engine(db_config: DBConfig) -> AsyncEngine:
    return create_async_engine(
        url=db_config.dsn,
        echo=db_config.is_echo
    )


def create_session_maker(engine: AsyncEngine) -> async_sessionmaker:
    pool: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    return pool


async def create_tables(engine: AsyncEngine):
    async with engine.begin() as conn:
        # db.async_engine.echo = False
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        engine.echo = True
