from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Psychology
from .getters import get_start

psychology_dialog = Dialog(
    Window(
        Format('{dlg_psychology}'),
        StaticMedia(
            path='resources/images/psychology.jpg',
            type=ContentType.PHOTO
        ),
        getter=get_start,
        state=Psychology.start,
    )
)
