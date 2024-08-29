from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Psychology
from .callbacks import (
    btn_psychology_start_session_clicked,
    btn_back_clicked,
)
from .getters import get_start

psychology_dialog = Dialog(
    Window(
        Format('{win_psychology_start}'),
        StaticMedia(
            path='resources/images/psychology.jpg',
            type=ContentType.PHOTO
        ),
        Row(
            Button(
                text=Format('{btn_psychology_start_session}'),
                id='btn_psychology_start_session',
                on_click=btn_psychology_start_session_clicked,
            ),
            Button(
                text=Format('{btn_back}'),
                id='btn_back',
                on_click=btn_back_clicked,
            ),
        ),
        getter=get_start,
        state=Psychology.start,
    )
)
