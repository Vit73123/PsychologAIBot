from logging import getLogger

from sqlalchemy import select, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from tgbot.db import Status
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class StatusRepo:
    pool: async_sessionmaker[AsyncSession]

    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    # Получить состояние пользователя по id состояния
    async def get(self, id_: int) -> Status | None:
        log.debug(" Repo: get status: id=%s", id_)

        async with self.pool() as session:
            status = await session.get(Status, id_)

            log.debug(" Repo: get status: %s", status)
        return status

    # Получить последнее состояние данного пользователя по его user_id в базе данных
    async def get_last_by_user_id(self, user_id: int) -> Status | None:
        log.debug(" Repo: get last status by db_user_id=%s", user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(Status)
                .filter(and_(
                    Status.user_id == user_id))  # Idea: должен быть столбец bool, а не выражение. Можно игнорировать
                .order_by(Status.updated_at.desc())
                .limit(1)
            )
            status = result.one_or_none()

            return status

    # Получить все состояния данного пользователя по его user_id в базе данных
    async def get_all_by_user_id(self, user_id: int):
        log.debug(" Repo: get all statuses by db_user_id=%s", user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(Status)
                .filter(and_(Status.user_id == user_id))  # and_ - Функция SQLAlchemy
                # только для того, чтобы IDEA не ругалась на то, что
                # в where не столбец bool, а условное выражение
                .order_by(Status.updated_at.desc())
            )
            statuses = result.unique().all()

            log.debug(" Repo: statuses: %s", statuses)

        return statuses

    # Добавить состояние для данного пользователя по его user_id
    async def add(self, status: Status) -> Status:
        log.debug(" Repo: add status: %s", status)

        async with self.pool() as session:
            session.add(status)
            await session.commit()
        return status

    # Изменить состояние
    async def update(self, status: Status) -> None:
        log.debug(" Repo: update status: %s", status)

        async with self.pool() as session:
            db_status = await session.get(Status, status.id)

            db_status.user_id = status.user_id
            db_status.text = status.text
            db_status.grade = status.grade

            await session.commit()

            log.debug(" Repo: status: %s", db_status)

    # Удалить состояние
    async def delete(self, status_id: int) -> None:
        log.debug(" Repo: delete status id=%s", status_id)

        async with self.pool() as session:
            user = await session.get(Status, status_id)

            await session.delete(user)
            await session.commit()

    # Удалить последнее состояние данного пользователя по его user_id в базе данных
    async def delete_last_by_user_id(self, user_id: int) -> None:
        log.debug(" Repo: delete last status by db_user_id=%s", user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(Status)
                .filter(and_(Status.user_id == user_id))
                .order_by(Status.updated_at.desc())
                .limit(1)
            )
            status = result.one_or_none()
            if status:
                await session.delete(status)
                await session.commit()

    # Удалить все состояния данного пользователя по его user_id в базе данных
    async def delete_all_by_user(self, user_id: int) -> None:
        log.debug(" Repo: delete all statuses by db_user_id=%s", user_id)

        async with self.pool() as session:
            query = delete(Status).where(and_(Status.user_id == user_id))
            await session.execute(query)
            await session.commit()
