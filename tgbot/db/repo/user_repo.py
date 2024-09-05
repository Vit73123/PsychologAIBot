from logging import getLogger

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import selectinload

from tgbot.db.dao import UserDAO
from tgbot.db.models import User
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.user_utils import create_user_to_dao

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class UserRepo:
    pool: async_sessionmaker[AsyncSession]

    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    # Регистрация пользователя
    async def register(self, bot_user: User) -> UserDAO | None:
        log_dev.debug(" Repo: register bot user: %s", bot_user)

        user = await self._get_by_bot_user_id_to_user(bot_user.user_id)

        if not user:
            user = await self._add(bot_user)
        elif user != bot_user:
            log.warning(" Repo: set user error: User data changed and should be updated.")
        log.debug(" Repo: user: %s", user)
        return create_user_to_dao(user)

    # Получить пользователя по id базы данных (из общего контекста бота)
    async def get(self, user_id: int) -> UserDAO | None:
        log.debug(" Repo: get user: id=%s", user_id)

        async with self.pool() as session:
            user = await session.get(User, user_id)

            log.debug(" Repo: get user: %s", user)
        return create_user_to_dao(user)

    # Получить пользователя по user_id телеграмма
    async def get_by_bot_user_id(self, bot_user_id: int) -> UserDAO | None:
        log.debug(" Repo: get user by user_id: user_id=%s", bot_user_id)

        user = await self._get_by_bot_user_id_to_user(bot_user_id)
        return create_user_to_dao(user)

    # Получить пользователя по user_id телеграмма
    async def _get_by_bot_user_id_to_user(self, bot_user_id: int) -> User | None:
        log.debug(" Repo: get user model by user_id: user_id=%s", bot_user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(User)
                .filter(and_(User.user_id == bot_user_id))
            )
            user = result.one_or_none()
            return user

    # Получить пользователя и все его статусы, отсортированные по убыванию даты
    async def _get_with_all_statuses_to_user(self, user_id: int) -> User | None:
        log.debug(" Repo: get user with all statuses id=: %s", user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(User)
                .options(selectinload(User.statuses))
                .filter(and_(User.id == user_id))  # and_ - Функция SQLAlchemy
                # только для того, чтобы IDEA не ругалась на то, что
                # в where не столбец bool, а условное выражение
            )
            db_user = result.unique().one_or_none()

            log.debug(" Repo: user: %s", db_user)
            log.debug(" Repo: statuses: %s", db_user.statuses)

        return db_user

    # Добавить нового пользователя
    async def _add(self, user: User) -> User | None:
        log.debug(" Repo: add user: %s", user)

        async with self.pool() as session:
            session.add(user)

            await session.commit()
        return user

    # Изменить пользователя
    async def update(self, user_dao: UserDAO) -> None:
        log.debug(" Repo: update user: %s", user_dao)

        async with self.pool() as session:
            user = await session.get(User, user_dao.id)

            log.debug(" Repo: update db user: %s", user)

            user.name = user_dao.name
            user.gender = user_dao.gender
            user.age = user_dao.age
            await session.commit()

    # Удалить пользователя
    async def delete(self, user_id: int) -> None:
        log.debug(" Repo: delete user id=%s", user_id)

        async with self.pool() as session:
            user = await session.get(User, user_id)

            await session.delete(user)
            await session.commit()
