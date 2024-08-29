import logging

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.kbd import Button

from tgbot.dialogs.states import Start
from tgbot.services.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def btn_profile_start_aboutme_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: about me")
    await dialog_manager.next(show_mode=ShowMode.SEND)


async def btn_back_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: back to Start dialog")
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


async def btn_profile_aboutme_name_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: name")


async def btn_profile_aboutme_male_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: male")


async def btn_profile_aboutme_female_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: female")


async def btn_profile_aboutme_age_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: age")


async def btn_ok_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: ok")


async def btn_cancel_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: cancel")
