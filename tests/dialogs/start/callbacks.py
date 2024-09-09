from aiogram.types import CallbackQuery
from aiogram_dialog.widgets.kbd import Button

from tests.dialogs.states import *
from tests.utils.dialog_utils import *
from tgbot.tools.logger import get_logger_dev

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def btn_test_check_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Test: btn_test_click: context: %s", dialog_manager.current_context())

    log_dev.debug(" Test: btn_test_click: inp_test: %s",
                  item_get_value(item_id='inp_test', dialog_manager=dialog_manager))
    log_dev.debug(" Test: btn_test_click: radio_test: %s",
                  item_get_value(item_id='radio_test', dialog_manager=dialog_manager))


async def btn_test_set_click(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    log_dev.debug(" Test: btn_test_click: context: %s", dialog_manager.current_context())

    log_dev.debug(" Test: btn_test_click: inp_test: %s",
                  item_set_value(item_id='inp_test', dialog_manager=dialog_manager))
    log_dev.debug(" Test: btn_test_click: radio_test: %s",
                  item_set_value(item_id='radio_test', dialog_manager=dialog_manager))

    await dialog_manager.switch_to(state=Start.start)


def inp_test_check(text: str) -> str:
    return text

# async def inp_test_success(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:


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
