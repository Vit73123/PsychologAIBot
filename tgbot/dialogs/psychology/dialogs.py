from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Cancel
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format, Const

from tgbot.dialogs.states import Psychology
from .callbacks import (
    btn_startappointment_clicked,
)
from .getters import get_start


# Психология
psychology_dialog = Dialog(
    Window(
        Format('{win_psychology}'),
        StaticMedia(
            path='resources/images/psychology.jpg',
            type=ContentType.PHOTO
        ),
        Button(
            text=Format('{btn_startappointment}'),
            id='btn_startappointment',
            on_click=btn_startappointment_clicked,
        ),
        Cancel(Format('{btn_getback_home}'), id='btn_getback_home'),
        getter=get_start,
        state=Psychology.start,
    )
)
