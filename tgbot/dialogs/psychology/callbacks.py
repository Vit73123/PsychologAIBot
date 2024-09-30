import logging

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from tgbot.dialogs.states import Psychology
from tgbot.tools.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def inp_message_check(text: str) -> str:
    log_dev.debug(" Message: input text: check")
    return text


async def inp_message_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager,
                              text: str) -> None:
    log_dev.debug(" Message: input text: succeed")

    await message.answer("...")

    await dialog_manager.switch_to(state=Psychology.appointment)


async def btn_appointment_stop(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Message: input text: succeed")

    await callback.message.answer("...")

    await dialog_manager.switch_to(state=Psychology.review)