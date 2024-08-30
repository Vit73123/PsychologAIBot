import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from tgbot.dialogs.states import MyTest, MyTest1
from tgbot.services.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command('t'))
async def cmd_psychology(message: Message, dialog_manager: DialogManager, **kwargs):
    log_dev.debug(' /t')
    await dialog_manager.start(state=MyTest.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='t1'))
async def cmd_psychology(message: Message, dialog_manager: DialogManager, **kwargs):
    log_dev.debug(' /t1')
    await dialog_manager.start(state=MyTest1.start)
