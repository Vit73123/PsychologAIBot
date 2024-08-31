import logging
import re
from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button, Radio
from fluentogram import TranslatorRunner

from tgbot.dialogs.states import Start, Aboutme
from tgbot.tools.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# О себе
async def btn_aboutme_back_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" About me: button clicked: back to: Start")
    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


async def btn_aboutme_profile_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" About me: button clicked: next: to Profile")
    await dialog_manager.next()


# Профиль
async def btn_profile_name_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: button clicked: name")
    await dialog_manager.next()
    # await dialog_manager.switch_to(state=Aboutme.name)


async def btn_profile_age_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: button clicked: age")
    await dialog_manager.switch_to(state=Aboutme.age)


async def btn_profile_save_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: button clicked: save")


async def btn_profile_state_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: button clicked: next: to Status")
    await dialog_manager.switch_to(state=Aboutme.state)


async def btn_profile_back_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Profile: button clicked: cancel")
    await dialog_manager.back()


# Пол
async def radio_gender_clicked(event: CallbackQuery, radio: Radio, dialog_manager: DialogManager, item_id: str):
    log_dev.info(" Gender: item selected: %s", item_id)


# Имя
async def btn_name_skip_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Name: button clicked: skip")
    await dialog_manager.back()


def inp_name_check(text: str) -> str:
    log_dev.info(" Name: input text: check")
    pattern = re.compile("^[a-zA-Zа-яА-ЯёЁ ]+$")
    if pattern.search(text):
        return text
    else:
        raise ValueError


async def inp_name_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                           text: str) -> None:
    log_dev.info(" Name: input text: succeed")
    log_dev.info(" Name: state: %s", dialog_manager.dialog_data.get('profile'))
    log_dev.info(" Name: context: %s", dialog_manager.current_context())

    dialog_manager.dialog_data.update(
        {'name': text}
    )
    log_dev.info(" Name: state: %s", dialog_manager.dialog_data.get('profile'))
    log_dev.info(" Name: context: %s", dialog_manager.current_context())
    await dialog_manager.switch_to(state=Aboutme.profile)


async def inp_name_error(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                         error: ValueError) -> None:
    log_dev.info(" Name: input text: error")
    i18n: TranslatorRunner = dialog_manager.middleware_data['i18n']
    await message.answer(
        i18n.win.aboutme.profile.name.error()
    )


# Возраст
async def btn_age_skip_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Age: button clicked: skip")
    await dialog_manager.back()


def inp_age_check(text: str) -> int:
    log_dev.info(" Age: input text: check")
    if text.isdigit() and (5 <= int(text) <= 150):
        return int(text)
    else:
        raise ValueError


async def inp_age_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    log_dev.info(" Age: input text: success")
    log_dev.info(" Age: state: %s", dialog_manager.dialog_data.get('profile'))
    log_dev.info(" Age: context: %s", dialog_manager.current_context())

    dialog_manager.dialog_data.update(
        {'age': int(text)}
    )
    log_dev.info(" Age: state: %s", dialog_manager.dialog_data.get('profile'))
    log_dev.info(" Age: context: %s", dialog_manager.current_context())
    await dialog_manager.switch_to(state=Aboutme.profile)


async def inp_age_error(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                        error: ValueError) -> None:
    log_dev.info(" Age: input text: error")
    i18n: TranslatorRunner = dialog_manager.middleware_data['i18n']
    await message.answer(
        i18n.win.aboutme.profile.age.error()
    )


# Состояние
async def btn_state_skip_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" State: button clicked: skip: to State")
    await dialog_manager.next()


async def btn_state_back_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" State: button clicked: back: to Profile")
    await dialog_manager.back()


async def inp_state_check(text: str) -> str:
    log_dev.info(" State: Input text: check")
    return text


async def inp_state_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                            text: str) -> None:
    log_dev.info(" State: Input text: succeed")
    await dialog_manager.next()


# Оценка
async def btn_grade_skip_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Grade: button clicked: skip: to Profile")
    await dialog_manager.next()


async def btn_grade_back_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.info(" Grade: button clicked: back: to State")
    await dialog_manager.back()
