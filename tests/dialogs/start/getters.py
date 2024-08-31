from logging import getLogger

from aiogram_dialog import DialogManager

from tgbot.db import Repo
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_start(dialog_manager: DialogManager, repo: Repo, **kwargs) -> dict[str, str]:
    log_dev.debug(" context: %s", dialog_manager.current_context())
    log.info(" Start: get_start")

    return {}
