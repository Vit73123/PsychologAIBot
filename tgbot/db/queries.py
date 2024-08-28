from logging import getLogger

from aiogram import types
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from tgbot.db.models import User
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_user_by_user_id(session_pool: async_sessionmaker, user_id: int) -> User:
    log.info("Get user by Telegram user_id=%s", str(user_id))
    async with session_pool() as session:
        query = (
            select(User)
            .filter(User.user_id == user_id)
        )
        result_ = await session.execute(query)
        result = result_.scalars().first()
        return result


async def insert_user(session_pool: async_sessionmaker, user: types.User) -> User:
    log_dev.info("Insert Bot User=%s", user)
    async with session_pool() as session:
        user_ = User(
            user_id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            name=user.username,
        )
        session.add(user_)
        await session.commit()
        return user_


async def create_if_new_user(session_pool: async_sessionmaker, user: types.User) -> User | None:
    log_dev.info("Create new user if not exists Bot User=%s", user)
    user_ = await get_user_by_user_id(session_pool, user.id)
    if not user_:
        return await insert_user(session_pool, user)
    return
