import logging
from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button
from fluentogram import TranslatorRunner

import re
from tgbot.dialogs.states import Start, Aboutme
from tgbot.services.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# О себе
async def btn_aboutme_back_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Button clicked: back to: Start")
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


async def btn_aboutme_profile_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" About me: Button clicked: next: to Profile")
    await dialog_manager.next()


# Профиль
async def btn_aboutme_profile_name_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: Button clicked: name")
    await dialog_manager.next()


async def btn_aboutme_profile_age_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: Button clicked: age")
    await dialog_manager.switch_to()


async def btn_aboutme_profile_save_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: Button clicked: save")


async def btn_aboutme_profile_state_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: Button clicked: next: to Status")
    await dialog_manager.next()


async def btn_aboutme_profile_back_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: Button clicked: cancel")
    await dialog_manager.back()


# Имя
async def btn_aboutme_profile_name_skip_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Name: Button clicked: skip")
    await dialog_manager.back()


def inp_name_check(text: str) -> str:
    log_dev.info(" Name: Input text: check")
    pattern = re.compile("^[a-zA-Zа-яА-ЯёЁ ]+$")
    if pattern.search(text):
        return text
    else:
        raise ValueError


async def inp_name_success(message: Message,
                           widget: ManagedTextInput,
                           dialog_manager: DialogManager,
                           text: str) -> None:
    log_dev.info(" Name: Input text: succeed")
    await dialog_manager.switch_to(Aboutme.profile)


async def inp_name_error(message: Message,
                         widget: ManagedTextInput,
                         dialog_manager: DialogManager,
                         error: ValueError) -> None:
    log_dev.info(" Name: Input text: error")
    i18n: TranslatorRunner = dialog_manager.middleware_data['i18n']
    await message.answer(
        i18n.win.aboutme.profile.name.error()
    )


# Возраст
async def btn_aboutme_profile_age_skip_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Age: Button clicked: skip")
    await dialog_manager.back()


def inp_age_check(text: str) -> int:
    log_dev.info(" Age: Input text: check")
    if text.isdigit() and (5 <= int(text) <= 150):
        return int(text)
    else:
        raise ValueError


async def inp_age_success(message: Message,
                          widget: ManagedTextInput,
                          dialog_manager: DialogManager,
                          text: str) -> None:
    log_dev.info(" Age: Input text: error")
    await dialog_manager.switch_to(Aboutme.profile)


async def inp_age_error(message: Message,
                        widget: ManagedTextInput,
                        dialog_manager: DialogManager,
                        error: ValueError) -> None:
    log_dev.info(" Age: Input text: error")
    i18n: TranslatorRunner = dialog_manager.middleware_data['i18n']
    await message.answer(
        i18n.win.aboutme.profile.age.error()
    )


# Состояние
async def btn_aboutme_profile_state_skip_clicked(callback: CallbackQuery, button: Button,
                                                 dialog_manager: DialogManager):
    log_dev.info(" Profile: Button clicked: skip: to State")
    await dialog_manager.next()


async def btn_aboutme_profile_state_back_clicked(callback: CallbackQuery, button: Button,
                                                 dialog_manager: DialogManager):
    log_dev.info(" Profile: Button clicked: back: to Profile")
    await dialog_manager.back()


async def inp_state_check(text: str) -> str:
    log_dev.info(" State: Input text: check")
    return text


async def inp_state_success(message: Message,
                            widget: ManagedTextInput,
                            dialog_manager: DialogManager,
                            text: str) -> None:
    log_dev.info(" State: Input text: succeed")
    await dialog_manager.next()


# Оценка
async def btn_aboutme_profile_grade_skip_clicked(callback: CallbackQuery, button: Button,
                                                 dialog_manager: DialogManager):
    log_dev.info(" Grade: Button clicked: skip: to Profile")
    await dialog_manager.next()


async def btn_aboutme_profile_grade_back_clicked(callback: CallbackQuery, button: Button,
                                                 dialog_manager: DialogManager):
    log_dev.info(" Grade: Button clicked: back: to State")
    await dialog_manager.back()
