from logging import getLogger

from sqlalchemy import select, and_, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from tgbot.db.dao import AppointmentDAO
from tgbot.db.models import Appointment
from tgbot.tools.logger import get_logger_dev
from tgbot.utils import create_appointment_to_dao, create_appointment_from_dao

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class AppointmentRepo:
    pool: async_sessionmaker[AsyncSession]

    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    # Получить сеанс пользователя по id сеанс
    async def get(self, id_: int) -> AppointmentDAO | None:
        log.debug(" Repo: get appointment: id=%s", id_)

        async with self.pool() as session:
            appointment = await session.get(Appointment, id_)

            log.debug(" Repo: get appointment: %s", appointment)
        return create_appointment_to_dao(appointment)

    # Получить последний сеанс данного пользователя по его user_id в базе данных
    async def get_last_by_user_id(self, user_id: int) -> AppointmentDAO | None:
        log.debug(" Repo: get last appointment by db_user_id=%s", user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(Appointment)
                .filter(and_(
                    Appointment.user_id == user_id))  # Idea: должен быть столбец bool, а не выражение. Можно игнорировать
                .order_by(Appointment.updated_at.desc())
                .limit(1)
            )
            appointment = result.one_or_none()

            return create_appointment_to_dao(appointment)

    # Получить все сеансы данного пользователя по его user_id в базе данных
    async def get_all_by_user_id(self, user_id: int) -> list[AppointmentDAO]:
        log.debug(" Repo: get all appointments by db_user_id=%s", user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(Appointment)
                .filter(and_(Appointment.user_id == user_id))  # and_ - Функция SQLAlchemy
                # только для того, чтобы IDEA не ругалась на то, что
                # в where не столбец bool, а условное выражение
                .order_by(Appointment.updated_at.desc())
            )
            appointments = result.unique().all()

            log.debug(" Repo: appointments: %s", appointments)

            appointments_list = list(map(create_appointment_to_dao, appointments))
        return appointments_list

    # Добавить сеанс для данного пользователя по его user_id
    async def add(self, appointment_dao: AppointmentDAO) -> AppointmentDAO | None:
        log.debug(" Repo: add appointment: %s", appointment_dao)
        appointment: Appointment = create_appointment_from_dao(appointment_dao)

        async with self.pool() as session:
            session.add(appointment)
            await session.commit()
        return create_appointment_to_dao(appointment)

    # Изменить сеанс
    async def update(self, appointment_dao: AppointmentDAO) -> None:
        log.debug(" Repo: update appointment: %s", appointment_dao)
        appointment = create_appointment_from_dao(appointment_dao)

        async with self.pool() as session:
            appointment = await session.get(Appointment, appointment.id)

            appointment.review = appointment_dao.review

            await session.commit()

            log.debug(" Repo: appointment: %s", str(appointment))

    # Удалить сеанс
    async def delete(self, appointment_id: int) -> None:
        log.debug(" Repo: delete appointment id=%s", appointment_id)

        async with self.pool() as session:
            user = await session.get(Appointment, appointment_id)

            await session.delete(user)
            await session.commit()

    # Удалить последний сеанс данного пользователя по его user_id в базе данных
    async def delete_last_by_user_id(self, user_id: int) -> None:
        log.debug(" Repo: delete last appointment by db_user_id=%s", user_id)

        async with self.pool() as session:
            result = await session.scalars(
                select(Appointment)
                .filter(and_(Appointment.user_id == user_id))
                .order_by(Appointment.updated_at.desc())
                .limit(1)
            )
            appointment = result.one_or_none()
            if appointment:
                await session.delete(appointment)
                await session.commit()

    # Удалить все сеансы данного пользователя по его user_id в базе данных
    async def delete_all_by_user(self, user_id: int) -> None:
        log.debug(" Repo: delete all appointmentes by db_user_id=%s", user_id)

        async with self.pool() as session:
            query = delete(Appointment).where(and_(Appointment.user_id == user_id))
            await session.execute(query)
            await session.commit()
