import logging

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from tgbot.dialogs.states import Start
from tgbot.services.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def btn_tests_start_choosetest_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug("Button clicked: Test")


async def btn_back_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug("Button clicked: Back to Start dialog")
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)
