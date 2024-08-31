from logging import getLogger

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

    async def get(self, id_: int) -> User | None:
        log.debug(" Repo: get user: id=%s", id_)

        async with self.pool() as session:
            user = await session.get(User, id_)
        return user

    async def add(self, user: User) -> User:
        log_dev.debug(" Repo: add user: %s", user)

        async with self.pool() as session:
            session.add(user)
            await session.commit()
            return user

    async def update(self, user: User) -> None:
        log_dev.debug(" Repo: update user: %s", user)

        async with self.pool() as session:
            user = session.get(user.id)
            await session.commit()
            log_dev.debug(" Repo: user: %s", user)

    async def get_by_bot_user_id(self, user_id: int) -> User | None:
        log.debug(" Repo: get user by user_id: user_id=%s", user_id)

        async with self.pool() as session:
            query = (
                select(User)
                .filter(User.user_id == user_id)    # Idea: должен быть столбец bool, а не выражение. Можно игнорировать
            )
            result_ = await session.execute(query)
            result = result_.scalars().one_or_none()
            return result
