from logging import getLogger

from aiogram import types
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker

from tgbot.db.models import User
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_user_by_user_id(session_pool: async_sessionmaker, tg_user_id: int) -> User:
    log.info(" Get user: id=%s", tg_user_id)
    async with session_pool() as session:
        query = (
            select(User)
            .filter(User.user_id == tg_user_id)
        )
        result_ = await session.execute(query)
        result = result_.scalars().first()
        return result


async def insert_user(session_pool: async_sessionmaker, tg_user: types.User) -> User:
    log.info(" Insert user: id=%s", tg_user.id)
    async with session_pool() as session:
        user = User(
            user_id=tg_user.id,
            username=tg_user.username,
            first_name=tg_user.first_name,
            last_name=tg_user.last_name,
            name=tg_user.username,
        )
        session.add(user)
        await session.commit()
        return user



