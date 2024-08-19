from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Profile
from .callbacks import (
    btn_create_profile_clicked,
    btn_back_clicked,
)
from .getters import get_start

profile_dialog = Dialog(
    Window(
        Format('{dlg_profile}'),
        StaticMedia(
            path='resources/images/profile.jpg',
            type=ContentType.PHOTO
        ),
        Row(
            Button(
                text=Format('{btn_create_profile}'),
                id='btn_create_profile',
                on_click=btn_create_profile_clicked,
            ),
            Button(
                text=Format('{btn_back}'),
                id='btn_back',
                on_click=btn_back_clicked,
            ),
        ),
        getter=get_start,
        state=Profile.start,
    )
)
