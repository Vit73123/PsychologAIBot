from logging import getLogger

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from tgbot.db import Status
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class StatusRepo:
    pool: async_sessionmaker[AsyncSession]

    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    # Получить состояние пользователя по id
    async def get(self, id_: int) -> Status | None:
        log.debug(" Repo: get status: id=%s", id_)

        async with self.pool() as session:
            status = await session.get(Status, id_)

            log.debug(" Repo: get status: %s", status)
        return status

    #
    async def get_last_by_user_id(self, user_id: int) -> Status | None:
        log.debug(" Repo: get last status by db_user_id: user_id=%s", user_id)

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

    async def add(self, status: Status) -> Status:
        log.debug(" Repo: add status: %s", status)

        async with self.pool() as session:
            session.add(status)
            await session.commit()
        return status

    async def update(self, status: Status) -> None:
        log.debug(" Repo: update status: %s", status)

        async with self.pool() as session:
            db_status = await session.get(Status, status.id)

            db_status.user_id = status.user_id
            db_status.text = status.text
            db_status.grade = status.grade

            await session.commit()

            log.debug(" Repo: status: %s", db_status)

    async def delete(self, status_id: int) -> None:
        log.debug(" Repo: delete status id=%s", status_id)

        async with self.pool() as session:
            user = await session.get(Status, status_id)

            await session.delete(user)
            await session.commit()

