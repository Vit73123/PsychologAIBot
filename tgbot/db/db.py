from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from tgbot.config.config import DatabaseConfig


class Db:
    engine: Engine
    session: async_sessionmaker


db: Db = Db()


def setup_db(db_config: DatabaseConfig) -> None:
    engine = create_async_engine(
        url=db_config.dsn,
        echo=db_config.is_echo
    )
    session = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    db.engine = engine
    db.session = session
