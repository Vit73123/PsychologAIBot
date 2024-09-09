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
from tgbot.utils.db import create_user_from_bot
from tgbot.utils.dialogs import reset_fsm, create_show_name_string

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, repo: Repo,
                    state: FSMContext, i18n: TranslatorRunner, **kwargs):
    log_dev.debug(' /start: Register user')

    # Первый запуск бота: состояние default (state=None)
    if not await state.get_state():
        # Регистрация пользователя: добавить в общий контекст бота его id из базы данных
        user_db = create_user_from_bot(message.from_user)
        user = await repo.user.register(user_db)

        # Общий контекст FSM, который должен сохраняться при перезагрузке диалогов
        state_data = {
            'user_data': {
                'user_id': user.id,
                'user_name': user.name,
            }
        }

        # Переключаем бота в рабочее состояние

        # Переход по команде /start в рабочем состоянии бота: not default (state=not None)
    else:

        # Перезагрузка диалогов:
        # - очищаем контекст FSM;
        # - сохраняем общий контекст FSM, необходимый для всех диалогов
        await reset_fsm(state)
        state_data = await state.get_data()

    await state.set_state(Start.start)
    await state.set_data(state_data)
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK, data=state_data['user_data'])
