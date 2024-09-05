import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from fluentogram import TranslatorRunner

from tgbot.db import Repo
from tgbot.dialogs.states import Start
from tgbot.tools.logger import get_logger_dev
from tgbot.utils import create_user_from_bot, create_user_name_text

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def cmd_start(message: Message, dialog_manager: DialogManager, repo: Repo,
                    state: FSMContext, i18n: TranslatorRunner, **kwargs):
    log_dev.debug(' /start: Register user')

    # Регистрация пользователя: добавить в общий контекст бота его id из базы данных
    user_db = create_user_from_bot(message.from_user)
    user = await repo.user.register(user_db)
    # Общий контекст FSM, который должен сохраняться при перезагрузке диалогов
    context = {
        'user_id': user.id,
        'user_name': create_user_name_text(user.name, i18n),
        'default_state': True,
    }

    await state.set_data({'context': context})
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK, data=context)


@router.message(CommandStart(), ~StateFilter(default_state))
async def cmd_start(message: Message, dialog_manager: DialogManager, state: FSMContext, **kwargs):
    log_dev.debug(' /start')

    # Перезагрузка диалогов после перехода в старт из любого другого диалога или по команде /start
    # Очищаем контекст FSM. Сохраняем общий контекст FSM, необходимый для всех диалогов
    data = await state.get_data()
    context = data['context']
    await state.clear()

    await state.set_data({'context': context})
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK, data=context)
