from logging import getLogger

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from tgbot.db.models import User
from tgbot.tools.logger import get_logger_dev

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
            log.debug(" Repo: get user: %s", user)
        return user

    async def add(self, user: User) -> User:
        log.debug(" Repo: add user: %s", user)

        async with self.pool() as session:
            session.add(user)
            await session.commit()
        return user

    async def delete(self, id_: int) -> None:
        log.debug(" Repo: delete user id=%s", id_)

        async with self.pool() as session:
            user = await session.get(User, id_)
            await session.delete(user)
            await session.commit()

    async def update(self, user: User) -> None:
        log.debug(" Repo: update user: %s", user)

        async with self.pool() as session:
            db_user = await session.get(User, user.id)

            log.debug(" Repo: update db user: %s", db_user)

            db_user.user_id = user.user_id
            db_user.username = user.username
            db_user.first_name = user.first_name
            db_user.last_name = user.last_name
            db_user.name = user.name
            db_user.gender = user.gender
            db_user.age = user.age
            await session.commit()

            log.debug(" Repo: user: %s", db_user)

    async def set(self, user: User) -> User:
        log.debug(" Repo: set user: %s", user)

        db_user = await self.get_by_bot_user_id(user.user_id)
        if not db_user:
            db_user = await self.add(user)
        elif user != db_user:
            log_dev.error(" Repo: set user error: Corrupted user: should be updated!")
        log.debug(" Repo: user: %s", db_user)
        return db_user

    async def get_with_statuses(self, id_: int):
        log_dev.debug(" Repo: get user with statuses id=: %s", id_)

    async def get_by_bot_user_id(self, user_id: int) -> User | None:
        log.debug(" Repo: get user by user_id: user_id=%s", user_id)

        async with self.pool() as session:
            query = (
                select(User)
                .filter(User.user_id == user_id)  # Idea: должен быть столбец bool, а не выражение. Можно игнорировать
            )
            result_ = await session.execute(query)
            result = result_.scalars().one_or_none()
            return result
