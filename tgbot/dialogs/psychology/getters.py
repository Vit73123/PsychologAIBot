from logging import getLogger
from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.tools.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

# Психология
async def get_start(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log.debug(" Psychology: get_start: context: %s", dialog_manager.current_context())

    return {
        "win_psychology_start": i18n.win.psychology(),
        "btn_psychology_startsession": i18n.btn.psychology.startsession(),
        "btn_psychology_getback_home": i18n.btn.getback.home(),
    }
