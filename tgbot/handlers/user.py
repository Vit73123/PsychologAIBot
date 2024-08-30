import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from tgbot.dialogs.states import Start
from tgbot.services.logger import get_logger_dev
from tgbot.services.user import create_user

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, state: FSMContext, **kwargs):
    log.info(' /start')

    data = state.get_state()
    # TODO: state from handler arguments
    # await create_user(message.from_user, **kwargs)

    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)
