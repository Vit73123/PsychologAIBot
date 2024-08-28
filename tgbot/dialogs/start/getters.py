from logging import getLogger
from pprint import pprint
from typing import TYPE_CHECKING

from fluentogram import TranslatorRunner

from tgbot.services.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_start(
        i18n: TranslatorRunner,
        session: dict,
        **kwargs
) -> dict[str, str]:
    return {
        "dlg_start": i18n.dlg.start(),
        "username": session['user_data']["username"]
    }
