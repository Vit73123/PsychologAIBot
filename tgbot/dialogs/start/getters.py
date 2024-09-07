from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.dialogs.states import Start
from tgbot.tools.logger import get_logger_dev

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

    # Очищаем контекст FSM, если переход из диалогов
    # Не очищаем машину состояний FSM, если переход после запуска бота, т.е. регистрации пользователя,
    # и переключаем состояние FSM по умолчанию
    state_data = await state.get_data()
    context = state_data.get('context')
    if context['default_state']:
        context['default_state'] = False
    else:
        log_dev.debug(" Start: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())
        await state.clear()
        # Переключаем FSM в состояние не по умолчанию
        await state.set_data({'context': context})
        log_dev.debug(" Start: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    await state.set_state(Start.start)
    log_dev.debug(" Start: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    user_name = dialog_manager.start_data.get('user_name')

    return {
        'user_name': user_name,
        'win_start': i18n.win.start(),
        'btn_psychology': i18n.btn.start.psychology(),
        'btn_tests': i18n.btn.start.tests(),
        'btn_aboutme': i18n.btn.start.aboutme(),
    }
