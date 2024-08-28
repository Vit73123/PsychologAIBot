from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Profile
from .callbacks import (
    btn_about_me_clicked,
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
                text=Format('{btn_about_me}'),
                id='btn_about_me',
                on_click=btn_about_me_clicked,
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
