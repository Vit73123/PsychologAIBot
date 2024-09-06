import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager

from tgbot.db.dao import AppointmentDAO
from tgbot.db.repo import Repo
from tgbot.filters import IsAdmin
from tgbot.tools.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command(commands='appointment'))
async def cmd_any_appointment(message: Message, dialog_manager: DialogManager, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /appointment: from_user: %s', message.from_user)
    log.debug(' /appointment: state data: %s', await state.get_data())


@router.message(Command(commands='appointment_g'), IsAdmin())
async def cmd_get_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /appointment_g: get appointment id=1')

    appointment_id = 1

    # Получить состояние пользователя по id состояния
    appointment: AppointmentDAO = await repo.appointment.get(appointment_id)

    log.debug(' /appointment_g: appointment: %s', appointment)


@router.message(Command(commands='appointment_gl'), IsAdmin())
async def cmd_get_last_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /appointment_gl: get last appointment: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Получить последнее состояние данного пользователя по его user_id в базе данных
    appointment: AppointmentDAO = await repo.appointment.get_last_by_user_id(user_id)

    log.debug(' /appointment_gl: appointment: %s', appointment)


@router.message(Command(commands='appointment_ga'), IsAdmin())
async def cmd_get_all_by_user_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /appointment_ga: get all appointments: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Получить все состояния данного пользователя по его user_id в базе данных
    appointments: list[AppointmentDAO] = await repo.appointment.get_all_by_user_id(user_id)

    log.debug(' /appointment_ga: appointments: %s', appointments)


@router.message(Command(commands='appointment_a'), IsAdmin())
async def cmd_add_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log_dev.debug(' /appointment_a: add appointment: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    appointment = AppointmentDAO(
        review="New review",
        user_id=user_id
    )

    # Добавить сеанс для данного пользователя по его user_id
    await repo.appointment.add(appointment)

    db_appointment = await repo.appointment.get_last_by_user_id(user_id)
    log_dev.debug(' /appointment_a: appointment: %s', db_appointment)


@router.message(Command(commands='appointment_u'), IsAdmin())
async def cmd_update_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log_dev.debug(' /appointment_u: update id=1: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    appointment = AppointmentDAO(
        appointment_id=1,
        user_id=user_id,
        review="Updated appointment",
    )

    # Изменить состояние
    await repo.appointment.update(appointment)
    log_dev.debug(' /appointment_u: appointment: %s', await repo.appointment.get_last_by_user_id(user_id))


@router.message(Command(commands='appointment_d'))
async def cmd_delete_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /appointment_d: delete: id=1: from_user: %s', message.from_user)

    # data = await state.get_data()
    # appointment_id = data['appointment_id']
    appointment_id = 1

    # Удалить состояние
    await repo.appointment.delete(appointment_id)


@router.message(Command(commands='appointment_dl'))
async def cmd_delete_last_by_user_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /appointment_dl: delete last: from_user: %s', message.from_user)

    # data = await state.get_data()
    # appointment_id = data['appointment_id']
    user_id = 1

    # Удалить последнее состояние данного пользователя по его user_id в базе данных
    await repo.appointment.delete_last_by_user_id(user_id)


@router.message(Command(commands='appointment_da'))
async def cmd_delete_all_by_user_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /appointment_da: delete all: from_user: %s', message.from_user)

    # data = await state.get_data()
    # appointment_id = data['appointment_id']
    user_id = 1

    # Удалить все состояния данного пользователя по его user_id
    await repo.appointment.delete_all_by_user(user_id)
