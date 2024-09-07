import logging

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from tgbot.tools.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def btn_tests_dotest_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug("Button clicked: dotest")
