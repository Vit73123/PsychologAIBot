import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from fluentogram import TranslatorRunner

from tgbot.db import Repo
from tgbot.dialogs.states import Start
from tgbot.tools.logger import get_logger_dev
from tgbot.tools.jinja import escape_text
from tgbot.utils import create_user_from_bot

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, repo: Repo, state: FSMContext,
                    i18n: TranslatorRunner, **kwargs):
    log.debug(' /start')

    data = await state.get_data()

    if not data:
        # Регистрация пользователя: добавить в общий контекст бота его id из базы данных
        user_db = create_user_from_bot(message.from_user)
        user = await repo.user.register(user_db)

        user_name = escape_text(user.name) if user.name else user.name

        data = {'user': {
            'id': user.id,
            'name': user_name
        }}
        await state.set_data(data)

    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK, data={'user': data['user']})
