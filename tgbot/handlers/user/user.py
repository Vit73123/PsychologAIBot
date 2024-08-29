import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from tgbot.common import set_user
from tgbot.dialogs.states import Psychology, Tests, Profile, Start
from tgbot.services.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, **kwargs):
    log.info(' /start')

    await set_user(message.from_user, **kwargs)
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='psychology'))
async def cmd_psychology(message: Message, dialog_manager: DialogManager, **kwargs):
    log.debug(' /psychology')
    await dialog_manager.start(state=Psychology.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='tests'))
async def cmd_tests(message: Message, dialog_manager: DialogManager, **kwargs):
    log.debug(' /tests')
    await dialog_manager.start(state=Tests.start, mode=StartMode.RESET_STACK, )


@router.message(Command(commands='profile'))
async def cmd_profile(message: Message, dialog_manager: DialogManager, **kwargs):
    log.debug(' /profile')
    await dialog_manager.start(state=Profile.start, mode=StartMode.RESET_STACK)
