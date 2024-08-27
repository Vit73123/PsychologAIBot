from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
    AsyncEngine
)

from tgbot.config.config import DBConfig


def create_pool(db_config: DBConfig):
    engine = create_engine(db_config)
    return create_session_maker(engine)


def create_engine(db_config: DBConfig):
    return create_async_engine(
        url=db_config.dsn,
        echo=db_config.is_echo
    )


def create_session_maker(engine: AsyncEngine):
    pool: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    return pool
