import logging

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from tgbot.dialogs.states import Psychology, Tests, Aboutme
from tgbot.tools.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# Психология
async def btn_psychology_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Start: btn_psychology_click: context: %s", dialog_manager.current_context())

    await dialog_manager.start(state=Psychology.start, data={'user': dialog_manager.start_data['user']})


# Тесты
async def btn_tests_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Start: btn_tests_click: context: %s", dialog_manager.current_context())

    await dialog_manager.start(state=Tests.start, data={'user': dialog_manager.start_data['user']})


# О себе
async def btn_aboutme_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Start: btn_aboutme_click: context: %s", dialog_manager.current_context())

    await dialog_manager.start(state=Aboutme.start, data={'user': dialog_manager.start_data['user']})
