import logging

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

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

    await dialog_manager.switch_to(state=Psychology.appointment)
