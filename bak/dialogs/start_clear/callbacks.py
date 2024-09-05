import datetime
import logging

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from tgbot.tools.logger import get_logger_dev

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

async def btn_widget_clear_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" clear widget: context: %s", dialog_manager.current_context())

    dialog_manager.current_context().widget_data.clear()

    log_dev.debug(" clear widget: context: %s\n", dialog_manager.current_context())


async def btn_dialog_clear_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" clear dialog: context: %s", dialog_manager.current_context())

    dialog_manager.current_context().dialog_data.clear()

    log_dev.debug(" clear dialog: context: %s\n", dialog_manager.current_context())


async def btn_all_dialog_clear_clicked(callback: CallbackQuery, button: Button,
                                       dialog_manager: DialogManager):
    log_dev.debug(" clear all dialog: context: %s", dialog_manager.current_context())

    dialog_manager.dialog_data.clear()

    log_dev.debug(" clear all dialog: context: %s\n", dialog_manager.current_context())


async def btn_add_widget_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" add data: context: %s", dialog_manager.current_context())

    dialog_manager.current_context().widget_data.update({f"{datetime.datetime.now().time().microsecond}": "a"})

    log_dev.debug(" add data: context: %s\n", dialog_manager.current_context())


async def btn_add_dialog_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" add data: context: %s", dialog_manager.current_context())

    dialog_manager.current_context().dialog_data.update({f"{datetime.datetime.now().time().microsecond}": "b"})

    log_dev.debug(" add data: context: %s\n", dialog_manager.current_context())


async def btn_add_all_dialog_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" add data: context: %s", dialog_manager.current_context())

    dialog_manager.dialog_data.update({f"{datetime.datetime.now().time().microsecond}": "c"})

    log_dev.debug(" add data: context: %s\n", dialog_manager.current_context())
