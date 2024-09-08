from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.dialogs.states import Start
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.dialogs import reset_fsm

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# Старт
async def get_start(dialog_manager: DialogManager,
                    state: FSMContext,
                    i18n: TranslatorRunner,
                    **kwargs
                    ) -> dict[str, str]:
    log_dev.debug(" Start: get_start: context: %s", dialog_manager.current_context())
    log_dev.debug(" Start: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    # Перезагрузка диалогов, если переход из другого диалога - не по команде /star (не из состояния start)
    # state_state = await state.get_state()
    if await state.get_state() != Start.start:
        await reset_fsm(state)
    # Установить состояние в dialog, если переход по команде /start (из состояния start)
    else:
        await state.set_state(Start.dialog)

    return {
        'user_name': dialog_manager.start_data['user_name_show'],
        'win_start': i18n.win.start(),
        'btn_psychology': i18n.btn.start.psychology(),
        'btn_tests': i18n.btn.start.tests(),
        'btn_aboutme': i18n.btn.start.aboutme(),
    }
