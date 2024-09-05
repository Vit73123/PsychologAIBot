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


# Тесты
async def get_start(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log.debug(" Tests: get_start: context: %s", dialog_manager.current_context())

    return {
        "win_tests": i18n.win.tests(),
        "btn_tests_dotest": i18n.btn.tests.start.dotest(),
        "btn_tests_getback_home": i18n.btn.getback.home(),
    }
