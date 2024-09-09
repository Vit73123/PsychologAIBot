import logging
import re
from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput, TextInput
from aiogram_dialog.widgets.kbd import Button, Radio
from fluentogram import TranslatorRunner

from tgbot.dialogs.states import Aboutme
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.dialogs import set_profile_empty

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# О себе ======================================================================================================

async def btn_aboutme_profile_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log.debug(" About me: button clicked: next: to Profile")
    await dialog_manager.next()


# Профиль =====================================================================================================

async def btn_profile_name_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: name: to Name")

    await dialog_manager.switch_to(state=Aboutme.name)


async def btn_profile_age_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: age: to Age")

    dialog_manager.dialog_data.update({'input_data': 'age'})
    await dialog_manager.switch_to(state=Aboutme.age)


async def btn_profile_gender_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: gender: to Gender")

    radio_gender: Radio = dialog_manager.find('gender')
    dialog_manager.dialog_data.update({'gender': radio_gender.get_checked()})
    await dialog_manager.switch_to(state=Aboutme.gender)


# -------------------------------------------------------------------------------------------------------------

async def btn_profile_status_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: status: to Status")

    dialog_manager.dialog_data.update({'input_data': 'status'})
    await dialog_manager.switch_to(state=Aboutme.status)


async def btn_profile_grade_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: grade: to Grade")
    await dialog_manager.switch_to(state=Aboutme.grade)


# -------------------------------------------------------------------------------------------------------------

async def btn_profile_ok_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: ok: to Aboutme")
    # TODO: Сохранение в базе данных, если данные изменялись: user_upd,status_upd
    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    if updated_items:
        log_dev.debug(" Profile: button clicked: ok: context: %s", dialog_manager.current_context())
    await dialog_manager.switch_to(Aboutme.profile)


async def btn_profile_setback_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: setback")
    # TODO: Восстановить первоначальные данные диалога: сбросить FSMContext user_upd
    dialog_manager.current_context().dialog_data.clear()
    dialog_manager.current_context().widget_data.clear()
    dialog_manager.dialog_data.update({'updated_items': set()})

    log_dev.debug(" Profile: button clicked: ok: context: %s", dialog_manager.current_context())

    await dialog_manager.switch_to(Aboutme.profile)


async def btn_profile_clear_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Profile: button clicked: clear")
    # TODO: Сбросить все данные диалога: сбросить FSMContext user
    log_dev.debug(" Profile: button clicked: clear: context: %s", dialog_manager.current_context())
    set_profile_empty(dialog_manager)
    log_dev.debug(" Profile: button clicked: clear: context: %s", dialog_manager.current_context())
    await dialog_manager.switch_to(Aboutme.profile)


# Имя =========================================================================================================

def inp_name_check(text: str) -> str:
    log_dev.debug(" Name: input text: check")
    pattern = re.compile("^[a-zA-Zа-яА-ЯёЁ ]+$")
    if pattern.search(text) or text == '':
        return text.strip()
    else:
        raise ValueError


async def inp_name_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                           text: str) -> None:
    log_dev.debug(" Name: input text: succeed")

    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    if 'name' not in updated_items:
        updated_items.add('name')
        dialog_manager.dialog_data.update({'updated_items': updated_items})

    await dialog_manager.switch_to(state=Aboutme.profile)


async def inp_name_error(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                         error: ValueError) -> None:
    log_dev.debug(" Name: input text: error")
    i18n: TranslatorRunner = dialog_manager.middleware_data['i18n']
    await message.answer(
        i18n.win.name.error()
    )


# -------------------------------------------------------------------------------------------------------------

async def btn_name_ok_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Name: button clicked: ok")


async def btn_name_setback_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Name: button clicked: setback")

    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    updated_items.discard('name')
    dialog_manager.dialog_data.update({'updated_items': updated_items})

    await dialog_manager.switch_to(state=Aboutme.profile)


async def btn_name_clear_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Name: button clicked: clear")

    inp_name: TextInput = dialog_manager.find('name')
    inp_name.set_widget_data(manager=dialog_manager, value=None)

    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    updated_items.add('name')
    dialog_manager.dialog_data.update({'updated_items': updated_items})
    await dialog_manager.back()


async def btn_name_cancel_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Name: button clicked: cancel")
    await dialog_manager.back()


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

async def btn_age_ok_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Age: button clicked: ok")


async def btn_age_setback_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Age: button clicked: setback")
    await dialog_manager.back()


async def btn_age_clear_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Age: button clicked: clear")
    await dialog_manager.back()


async def btn_age_cancel_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Age: button clicked: cancel")
    await dialog_manager.back()


# Пол =========================================================================================================

async def btn_gender_ok_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Gender: button clicked: ok")
    log_dev.debug(" Gender: context: %s", dialog_manager.current_context())

    dialog_manager.dialog_data.pop('gender')

    log_dev.debug(" Gender: context: %s", dialog_manager.current_context())
    await dialog_manager.switch_to(state=Aboutme.profile)


async def btn_gender_setback_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Gender: button clicked: setback")


async def btn_gender_clear_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
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


async def inp_status_check(text: str) -> str:
    log_dev.debug(" Status: Input text: check")
    return text


async def inp_status_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                             text: str) -> None:
    log_dev.debug(" Status: Input text: succeed")
    await dialog_manager.next()


# -------------------------------------------------------------------------------------------------------------

async def btn_status_ok_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Status: button clicked: ok")


async def btn_status_setback_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Status: button clicked: setback")
    await dialog_manager.back()


async def btn_status_clear_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Status: button clicked: clear")
    await dialog_manager.back()


async def btn_status_cancel_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Status: button clicked: cancel")
    await dialog_manager.back()


# Оценка ======================================================================================================

async def inp_grade_check(text: str) -> str:
    log_dev.debug(" Grade: Input text: check")
    return text


async def inp_grade_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                            text: str) -> None:
    log_dev.debug(" Grade: Input text: succeed")
    await dialog_manager.next()


# -------------------------------------------------------------------------------------------------------------

async def btn_grade_ok_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Grade: button clicked: ok")


async def btn_grade_setback_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Grade: button clicked: setback")
    await dialog_manager.back()


async def btn_grade_clear_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Grade: button clicked: clear")
    await dialog_manager.back()


async def btn_grade_cancel_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Grade: button clicked: cancel")
    await dialog_manager.back()
