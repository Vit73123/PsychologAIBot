from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.dialogs.states import Start
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.dialogs import reset_fsm, create_show_name_string

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

    # Перезагрузка диалогов, если переход из другого диалога - не по команде /start (не из состояния start)
    # state_state = await state.get_state()
    if await state.get_state() != Start.start:
        await reset_fsm(state)

        state_data = await state.get_data()
        dialog_manager.start_data.update({'user_name': state_data['user_data']['user_name']})
    # Установить состояние в dialog, если переход по команде /start (из состояния start)
    else:
        await state.set_state(Start.dialog)

    # Показывать 'Новый пользователь', если user_name=None
    show_user_name: str = create_show_name_string(name=dialog_manager.start_data['user_name'], i18n=i18n)

    return {
        'user_name': show_user_name,
        'win_start': i18n.win.start(),
        'btn_psychology': i18n.btn.start.psychology(),
        'btn_tests': i18n.btn.start.tests(),
        'btn_aboutme': i18n.btn.start.aboutme(),
    }
