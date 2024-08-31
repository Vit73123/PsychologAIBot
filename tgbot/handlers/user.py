import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from tgbot.db import Repo
from tgbot.dialogs.states import Start
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.user_utils import create_from_bot_user

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /start')

    data = await state.get_data()
    if not data:
        user = create_from_bot_user(message.from_user)
        user = await repo.user.set(user)
        await state.set_data({'user_id': user.id})

    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)
