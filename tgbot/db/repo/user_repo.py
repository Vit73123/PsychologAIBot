from logging import getLogger

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import selectinload

from tgbot.db.models import User
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class UserRepo:
    pool: async_sessionmaker[AsyncSession]

    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    async def get(self, user_id: int) -> User | None:
        log.debug(" Repo: get user: id=%s", user_id)

        async with self.pool() as session:
            user = await session.get(User, user_id)

            log.debug(" Repo: get user: %s", user)
        return user

    async def add(self, user: User) -> User:
        log.debug(" Repo: add user: %s", user)

        async with self.pool() as session:
            session.add(user)

            await session.commit()
        return user

    async def delete(self, user_id: int) -> None:
        log.debug(" Repo: delete user id=%s", user_id)

        async with self.pool() as session:
            user = await session.get(User, user_id)

            await session.delete(user)
            await session.commit()

    async def update(self, user: User) -> None:
        log.debug(" Repo: update user: %s", user)

        async with self.pool() as session:
            db_user = await session.get(User, user.id)

            log.debug(" Repo: update db user: %s", db_user)

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
            log.warning(" Repo: set user error: User data changed and should be updated.")
        log.debug(" Repo: user: %s", db_user)
        return db_user

    async def get_by_bot_user_id(self, bot_user_id: int) -> User | None:
        log.debug(" Repo: get user by user_id: user_id=%s", bot_user_id)

        async with self.pool() as session:
            query = (
                select(User)
                .filter(User.user_id == bot_user_id)  # Idea: должен быть столбец bool, а не выражение. Можно игнорировать
            )
            result_ = await session.execute(query)
            result = result_.scalars().one_or_none()
            return result

    async def get_with_all_statuses(self, user_id: int):
        log.debug(" Repo: get user with all statuses id=: %s", user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(User)
                .options(selectinload(User.statuses))
                .where(and_(User.id == user_id))  # and_ - Функция SQLAlchemy
                # только для того, чтобы IDEA не ругалась на то, что
                # в where не столбец bool, а условное выражение
            )
            user = result.unique().one_or_none()

            log.debug(" Repo: user: %s", user)
            log.debug(" Repo: statuses: %s", user.statuses)

        return user
