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