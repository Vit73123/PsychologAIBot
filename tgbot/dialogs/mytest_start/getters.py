from logging import getLogger

from aiogram_dialog import DialogManager

from tgbot.dialogs.states import MyTest
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_mytest(dialog_manager: DialogManager, **kwargs) -> dict[str, str]:
    state = MyTest.start
    return {}
