from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Start
from .getters import get_start

start_dialog = Dialog(
    Window(
        Format('{start}'),
        getter=get_start,
        state=Start.start,
    )
)
