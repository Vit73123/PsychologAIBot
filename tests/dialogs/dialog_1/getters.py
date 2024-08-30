from logging import getLogger

from aiogram_dialog import DialogManager

from tgbot.utils.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_dialog_1(dialog_manager: DialogManager, **kwargs) -> dict[str, str]:
    # pprint(dialog_manager.current_context())
    # pprint(dialog_manager.current_stack())
    # pprint(dialog_manager.middleware_data)
    # log_dev.debug(" context: %s", dialog_manager.current_context())
    log.info(" Dialog 1: get_dialog_1")

    return {}
