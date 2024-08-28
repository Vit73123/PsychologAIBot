from sqlalchemy.ext.asyncio import AsyncEngine

from tgbot.db.models.base import Base
from .user import UserRepo


class Repo:
    user: UserRepo = UserRepo()

    async def create_tables(self, engine: AsyncEngine):
        async with engine.begin() as conn:
            # db.async_engine.echo = False
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            engine.echo = True
