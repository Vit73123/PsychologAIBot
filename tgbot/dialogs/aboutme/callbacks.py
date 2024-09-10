import logging
import re
from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button, Radio
from fluentogram import TranslatorRunner

from tgbot.dialogs.states import Aboutme
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.dialogs import (item_reset,
                                 item_clear,
                                 item_set,
                                 profile_reset,
                                 profile_clear,
                                 update_user,
                                 save_status, )

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# О себе ======================================================================================================

async def btn_aboutme_profile_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log.debug(" About me: button clicked: next: to Profile")
    await dialog_manager.next()


# Профиль =====================================================================================================

async def btn_profile_name_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: name: to Name")

    await dialog_manager.switch_to(state=Aboutme.name)


async def btn_profile_age_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: age: to Age")

    await dialog_manager.switch_to(state=Aboutme.age)


async def btn_profile_gender_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: gender: to Gender")

    radio_gender: Radio = dialog_manager.find('gender')
    dialog_manager.dialog_data.update({'gender': radio_gender.get_checked()})
    await dialog_manager.switch_to(state=Aboutme.gender)


# -------------------------------------------------------------------------------------------------------------

async def btn_profile_status_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: status: to Status")

    await dialog_manager.switch_to(state=Aboutme.status)


async def btn_profile_grade_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: grade: to Grade")
    await dialog_manager.switch_to(state=Aboutme.grade)


# -------------------------------------------------------------------------------------------------------------

async def btn_profile_ok_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: ok: to Aboutme")

    await update_user(dialog_manager)
    await save_status(dialog_manager)

    await dialog_manager.back()


async def btn_profile_reset_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: reset")

    profile_reset(dialog_manager)
    await dialog_manager.switch_to(Aboutme.profile)


async def btn_profile_clear_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: clear")

    profile_clear(dialog_manager)
    await dialog_manager.switch_to(Aboutme.profile)


# Имя =========================================================================================================

def inp_name_check(text: str) -> str:
    log_dev.debug(" Name: input text: check")
    pattern = re.compile("^[a-zA-Zа-яА-ЯёЁ ]+$")
    if pattern.match(text) or text == '':
        return text.strip()
    else:
        raise ValueError


async def inp_name_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                           text: str) -> None:
    log_dev.debug(" Name: input text: succeed")

    item_set(value=text, item_id='name', dialog_manager=dialog_manager)


async def inp_name_error(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                         error: ValueError) -> None:
    log_dev.debug(" Name: input text: error")
    i18n: TranslatorRunner = dialog_manager.middleware_data['i18n']
    await message.answer(
        i18n.win.name.error()
    )


# -------------------------------------------------------------------------------------------------------------

async def btn_name_reset_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Name: button clicked: reset")

    item_reset(item_id='name', dialog_manager=dialog_manager)
    await dialog_manager.switch_to(state=Aboutme.name)


async def btn_name_clear_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Name: button clicked: clear")

    item_clear(item_id='name', dialog_manager=dialog_manager)
    await dialog_manager.switch_to(state=Aboutme.name)


async def btn_name_cancel_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Name: button clicked: cancel")

    item_reset(item_id='name', dialog_manager=dialog_manager)
    await dialog_manager.switch_to(state=Aboutme.profile)


# Возраст =====================================================================================================

def inp_age_check(text: str) -> int | str:
    log_dev.debug(" Age: input text: check")
    if text.isdigit() and (5 <= int(text) <= 150):
        return int(text)
    elif text == '':
        return ''
    else:
        raise ValueError


async def inp_age_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    log_dev.debug(" Age: input text: success")
    # log_dev.debug(" Age: state: %s", dialog_manager.dialog_data.get('aboutme'))
    # log_dev.debug(" Age: context: %s", dialog_manager.current_context())

    # dialog_manager.dialog_data.update(
    #     {'age': int(text)}
    # )
    # log_dev.debug(" Age: state: %s", dialog_manager.dialog_data.get('aboutme'))
    # log_dev.debug(" Age: context: %s", dialog_manager.current_context())
    await dialog_manager.switch_to(state=Aboutme.profile)


async def inp_age_error(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                        error: ValueError) -> None:
    log_dev.debug(" Age: input text: error")
    i18n: TranslatorRunner = dialog_manager.middleware_data['i18n']
    await message.answer(
        i18n.win.age.error()
    )


# -------------------------------------------------------------------------------------------------------------

async def btn_age_ok_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Age: button clicked: ok")


async def btn_age_reset_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Age: button clicked: reset")
    await dialog_manager.back()


async def btn_age_clear_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Age: button clicked: clear")
    await dialog_manager.back()


async def btn_age_cancel_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Age: button clicked: cancel")
    await dialog_manager.back()


# Пол =========================================================================================================

async def btn_gender_ok_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Gender: button clicked: ok")
    log_dev.debug(" Gender: context: %s", dialog_manager.current_context())

    dialog_manager.dialog_data.pop('gender')

    log_dev.debug(" Gender: context: %s", dialog_manager.current_context())
    await dialog_manager.switch_to(state=Aboutme.profile)


async def btn_gender_reset_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Gender: button clicked: reset")


async def btn_gender_clear_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Gender: button clicked: clear")
    log_dev.debug(" Gender: context: %s", dialog_manager.current_context())

    radio_gender: Radio = dialog_manager.find('gender')
    await radio_gender.set_checked(0)


async def btn_gender_cancel_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Gender: button clicked: ok")
    log_dev.debug(" Gender: context: %s", dialog_manager.current_context())

    radio_gender: Radio = dialog_manager.find('gender')
    await radio_gender.set_checked(
        dialog_manager.dialog_data.pop('gender')
    )

    log_dev.debug(" Gender: context: %s", dialog_manager.current_context())

    await dialog_manager.switch_to(state=Aboutme.profile)


# Состояние ===================================================================================================


def inp_status_check(text: str) -> str:
    log_dev.debug(" Status: input text: check")
    if text.isspace() or text.isdigit():
        raise ValueError
    else:
        return text.strip()


async def inp_status_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                             text: str) -> None:
    log_dev.debug(" Status: input text: succeed")

    item_set(value=text, item_id='status_text', dialog_manager=dialog_manager)


async def inp_status_error(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                           error: ValueError) -> None:
    log_dev.debug(" Status: input text: error")
    i18n: TranslatorRunner = dialog_manager.middleware_data['i18n']
    await message.answer(
        i18n.win.status.error()
    )


# -------------------------------------------------------------------------------------------------------------

async def btn_status_reset_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Status: button clicked: reset")

    item_reset(item_id='status_text', dialog_manager=dialog_manager)
    await dialog_manager.switch_to(state=Aboutme.status)


async def btn_status_clear_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Status: button clicked: clear")

    item_clear(item_id='status_text', dialog_manager=dialog_manager)
    await dialog_manager.switch_to(state=Aboutme.status)


async def btn_status_cancel_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Status: button clicked: cancel")

    item_reset(item_id='status_text', dialog_manager=dialog_manager)
    await dialog_manager.switch_to(state=Aboutme.profile)


# Оценка ======================================================================================================

async def inp_grade_check(text: str) -> str:
    log_dev.debug(" Grade: Input text: check")
    return text


async def inp_grade_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                            text: str) -> None:
    log_dev.debug(" Grade: Input text: succeed")
    await dialog_manager.next()


# -------------------------------------------------------------------------------------------------------------

async def btn_grade_ok_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Grade: button clicked: ok")


async def btn_grade_reset_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Grade: button clicked: reset")
    await dialog_manager.back()


async def btn_grade_clear_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Grade: button clicked: clear")
    await dialog_manager.back()


async def btn_grade_cancel_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Grade: button clicked: cancel")
    await dialog_manager.back()
