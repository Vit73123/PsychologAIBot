from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Cancel
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Psychology
from .callbacks import (
    btn_start_session_clicked,
)
from .getters import get_start


# Психология
psychology_dialog = Dialog(
    Window(
        Format('{win_psychology_start}'),
        StaticMedia(
            path='resources/images/psychology.jpg',
            type=ContentType.PHOTO
        ),
        Button(
            text=Format('{btn_psychology_start_session}'),
            id='btn_psychology_start_session',
            on_click=btn_start_session_clicked,
        ),
        Cancel(Format('{btn_back_start}'), id='btn_back_start'),
        getter=get_start,
        state=Psychology.start,
    )
)
