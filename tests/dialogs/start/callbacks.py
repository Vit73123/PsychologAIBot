import datetime
import logging

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from tgbot.tools.logger import get_logger_dev
from tests.dialogs import states

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# async def btn_dialog1_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     log_dev.debug(" Start: btn_dialog1_click: context: %s", dialog_manager.current_context())
#
#     user_data = dialog_manager.start_data['user']
#
#     log_dev.debug(" Start: btn_dialog1_click: context: %s", dialog_manager.current_context())
#
#     await dialog_manager.start(state=Dialog_1.start, data={'user': user_data})

# async def btn_psychology_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     log_dev.debug(" psychology: context: %s", dialog_manager.current_context())
#
#     await dialog_manager.start(state=states.Start.psychology)