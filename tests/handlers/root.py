import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from tests.dialogs.states import Start
from tgbot.db.repo.repo import Repo
from tgbot.services.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, **kwargs):
    log_dev.debug(' /start')
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='c'))
async def cmd_dialog_1(message: Message, dialog_manager: DialogManager, repo: Repo, **kwargs):
    log_dev.debug(' /c: create tables')
    await repo.create_tables()
