from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Profile
from .callbacks import (
    btn_profile_start_aboutme_clicked,
    btn_back_clicked,
    btn_profile_aboutme_name_clicked,
    btn_profile_aboutme_male_clicked,
    btn_profile_aboutme_female_clicked,
    btn_profile_aboutme_age_clicked,
    btn_ok_clicked,
    btn_cancel_clicked,
)
from .getters import (
    get_start,
    get_aboutme,
)

profile_dialog = Dialog(
    Window(
        Format('{win_profile_start}'),
        StaticMedia(
            path='resources/images/profile.jpg',
            type=ContentType.PHOTO
        ),
        Row(
            Button(
                text=Format('{btn_profile_start_aboutme}'),
                id='btn_profile_start_aboutme',
                on_click=btn_profile_start_aboutme_clicked,
            ),
            Button(
                text=Format('{btn_back}'),
                id='btn_back',
                on_click=btn_back_clicked,
            ),
        ),
        getter=get_start,
        state=Profile.start,
    ),
    Window(
        Format('{win_profile_aboutme}'),
        Row(
            Button(
                text=Format('{btn_profile_aboutme_name}'),
                id='btn_profile_aboutme_name',
                on_click=btn_profile_aboutme_name_clicked,
            ),
        ),
        Row(
            Button(
                text=Format('{btn_profile_aboutme_male}'),
                id='btn_profile_aboutme_male',
                on_click=btn_profile_aboutme_male_clicked,
            ),
            Button(
                text=Format('{btn_profile_aboutme_female}'),
                id='btn_profile_aboutme_female',
                on_click=btn_profile_aboutme_female_clicked,
            ),
        ),
        Row(
            Button(
                text=Format('{btn_profile_aboutme_age}'),
                id='btn_profile_aboutme_age',
                on_click=btn_profile_aboutme_age_clicked,
            ),
        ),
        Row(
            Button(
                text=Format('{btn_ok}'),
                id='btn_ok',
                on_click=btn_ok_clicked,
            ),
            Button(
                text=Format('{btn_cancel}'),
                id='btn_cancel',
                on_click=btn_cancel_clicked,
            ),
        ),
        getter=get_aboutme,
        state=Profile.about_me,
    )
)
