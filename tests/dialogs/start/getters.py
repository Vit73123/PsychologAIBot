from logging import getLogger

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from tgbot.db import Repo
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_start(dialog_manager: DialogManager,
                    state: FSMContext,
                    repo: Repo, **kwargs
                    ) -> dict[str, str]:
    log_dev.debug(" Start: get_start: context: %s", dialog_manager.current_context())

    return {
        'user': dialog_manager.start_data.get('user')
    }
