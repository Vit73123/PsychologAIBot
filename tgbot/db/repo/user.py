from logging import getLogger

from aiogram import types
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from tgbot.db.models import User
from tgbot.utils.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class UserRepo:
    pool: async_sessionmaker[AsyncSession]

    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    async def get_user(self, id: int) -> User:
        log.info(" Get user: id=%s", id)

        async with self.pool() as session:
            query = (
                select(User)
                .filter(User.user_id == id)
            )
            result_ = await session.execute(query)
            result = result_.scalars().first()
            return result

    async def insert_user(self, bot_user: types.User) -> User:
        log.info(" Insert user: id=%s", bot_user.id)

        async with self.pool() as session:
            user = User(
                user_id=bot_user.id,
                username=bot_user.username,
                first_name=bot_user.first_name,
                last_name=bot_user.last_name,
                name=bot_user.first_name,
            )
            session.add(user)
            await session.commit()
            return user

    async def update_user(self, bot_user: types.User) -> User:
        log_dev.info(" Update user: id=%s", bot_user.id)

        async with self.pool() as session:
            user = self.get_user(bot_user.id)

            log_dev.info(" user: %s", user)

    async def get_user_by_user_id(self, bot_user_id: int) -> User:
        log.info(" Get user by user_id: user_id=%s", bot_user_id)

        async with self.pool() as session:
            query = (
                select(User)
                .filter(User.user_id == bot_user_id)
            )
            result_ = await session.execute(query)
            result = result_.scalars().first()
            return result
