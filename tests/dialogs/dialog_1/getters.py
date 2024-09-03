from logging import getLogger
from pprint import pprint

from aiogram_dialog import DialogManager

from tgbot.db import Repo
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_dialog_1(dialog_manager: DialogManager, repo: Repo, **kwargs) -> dict[str, str]:
    log_dev.debug(" Dialog 1: get_dialog_1: context: %s", dialog_manager.current_context())

    user_id = dialog_manager.start_data['user']['id']
    user = await repo.user.get(user_id)

    print(user)

    return {}
