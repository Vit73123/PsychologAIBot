from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class AppointmentRepo:
    pool: async_sessionmaker[AsyncSession]

    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    # Получить сеанс пользователя по id сеанс
    # async def get(self, id_: int) -> AppointmentDAO | None:
    #     log.debug(" Repo: get appointment: id=%s", id_)
    #
    #     async with self.pool() as session:
    #         appointment = await session.get(Appointment, id_)
    #
    #         log.debug(" Repo: get appointment: %s", appointment)
    #     return create_appointment_to_dao(appointment)