import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import async_sessionmaker

from tgbot.dialogs.states import Start, Psychology, Tests, Profile
from tgbot.services.logger import get_logger_dev
from tgbot.db.queries import create_if_new_user

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, session_pool: async_sessionmaker):
    log.info('/start')
    user = message.from_user
    await create_if_new_user(session_pool, user)
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='psychology'))
async def cmd_psychology(message: Message, dialog_manager: DialogManager):
    log.debug('/psychology')
    await dialog_manager.start(state=Psychology.start)


@router.message(Command(commands='tests'))
async def cmd_psychology(message: Message, dialog_manager: DialogManager):
    log.debug('/tests')
    await dialog_manager.start(state=Tests.start)


@router.message(Command(commands='profile'))
async def cmd_psychology(message: Message, dialog_manager: DialogManager):
    log.debug('/profile')
    await dialog_manager.start(state=Profile.start)
