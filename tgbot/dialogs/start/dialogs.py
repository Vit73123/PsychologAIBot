from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.media import StaticMedia
from aiogram.types import ContentType

from tgbot.dialogs.states import Start
from .getters import get_start

start_dialog = Dialog(
    Window(
        Format('{dlg_start}'),
        StaticMedia(
            path='resources/images/start.png',
            type=ContentType.PHOTO
        ),
        getter=get_start,
        state=Start.start,
    )
)
