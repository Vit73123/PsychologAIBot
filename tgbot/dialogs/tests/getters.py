from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.tools.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# Тесты
async def get_tests(
        dialog_manager: DialogManager,
        state: FSMContext,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Tests: get_psychology: context: %s", dialog_manager.current_context())
    log_dev.debug(" Tests: get_psychology: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    return {
        "win_tests": i18n.win.tests(),
        "btn_tests_dotest": i18n.btn.tests.start.dotest(),
        "btn_tests_getback_home": i18n.btn.getback.home(),
    }
