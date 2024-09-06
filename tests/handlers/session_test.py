import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager

from tgbot.db.dao import SessionDAO
from tgbot.db.repo import Repo
from tgbot.filters import IsAdmin
from tgbot.tools.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command(commands='session'))
async def cmd_any_session(message: Message, dialog_manager: DialogManager, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /session: from_user: %s', message.from_user)
    log.debug(' /session: state data: %s', await state.get_data())

@router.message(Command(commands='session_g'), IsAdmin())
async def cmd_get_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /session_g: get session id=1')

    session_id = 1

    # Получить состояние пользователя по id состояния
    session: SessionDAO = await repo.session.get(session_id)

    log.debug(' /session_g: session: %s', session)