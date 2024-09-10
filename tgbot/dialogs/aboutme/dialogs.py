import operator

from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Row, Group, Cancel, Back, SwitchTo, Radio
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from .callbacks import *
from .getters import *


aboutme_dialog = Dialog(

    # О себе
    Window(
        Format('{win_aboutme}'),
        StaticMedia(
            path='resources/images/aboutme.jpg',
            type=ContentType.PHOTO
        ),
        Button(
            text=Format('{btn_aboutme_profile}'),
            id='btn_aboutme_profile',
            on_click=btn_aboutme_profile_click,
        ),
        Cancel(text=Format('{btn_aboutme_getback_home}'), id='btn_aboutme_getback_home'),
        getter=get_aboutme,
        state=Aboutme.start,
    ),

    # Профиль
    Window(

        Format('<b>{win_profile_aboutme}</b>\n'),
        Format('{win_profile_h_status}'),
        Format('{win_profile_status}\n'),
        Format('{win_profile_h_grade}'),
        Format('{win_profile_grade}'),
        Row(
            Button(
                text=Format('{btn_profile_name}'),
                id='btn_profile_name',
                on_click=btn_profile_name_click
            ),
            Button(
                text=Format('{btn_profile_age}'),
                id='btn_profile_age',
                on_click=btn_profile_age_click
            ),
            Button(
                text=Format('{btn_profile_gender}'),
                id='btn_profile_gender',
                on_click=btn_profile_gender_click
            ),
        ),
        Row(
            Button(
                text=Format('{btn_profile_status}'),
                id='btn_profile_status',
                on_click=btn_profile_status_click
            ),
            Button(
                text=Format('{btn_profile_grade}'),
                id='btn_profile_grade',
                on_click=btn_profile_grade_click
            ),
        ),
        Row(
            Button(
                text=Format('{btn_profile_ok}'),
                id='btn_profile_ok',
                on_click=btn_profile_ok_click
            ),
            Button(
                text=Format('{btn_profile_reset}'),
                id='btn_profile_reset',
                on_click=btn_profile_reset_click
            ),
            Button(
                text=Format('{btn_profile_clear}'),
                id='btn_profile_clear',
                on_click=btn_profile_clear_click
            ),
            Back(text=Format('{btn_profile_cancel}'), id='btn_profile_cancel'),
        ),
        getter=get_profile,
        state=Aboutme.profile,
    ),

    # Имя
    Window(
        Format("<b>{win_name} {txt_username}?</b>\n"),
        Format("{win_name_txt}"),
        TextInput(
            id="name",
            type_factory=inp_name_check,
            on_success=inp_name_success,
            on_error=inp_name_error,
        ),
        Row(
            SwitchTo(
                text=Format('{btn_name_ok}'),
                id='btn_name_ok',
                state=Aboutme.profile),
            Button(
                text=Format('{btn_name_reset}'),
                id='btn_name_reset',
                on_click=btn_name_reset_click
            ),
            Button(
                text=Format('{btn_name_clear}'),
                id='btn_name_clear',
                on_click=btn_name_clear_click
            ),
            Button(
                text=Format('{btn_name_cancel}'),
                id='btn_name_cancel',
                on_click=btn_name_cancel_click
            ),
        ),
        getter=get_name,
        state=Aboutme.name,
    ),

    # Возраст
    Window(
        Format("<b>{win_age_h} {txt_age}?</b>\n"),
        Format("{win_age_txt}"),
        TextInput(
            id="age",
            type_factory=inp_age_check,
            on_success=inp_age_success,
            on_error=inp_age_error,
        ),
        Row(
            SwitchTo(
                text=Format('{btn_age_ok}'),
                id='btn_age_ok',
                state=Aboutme.profile),
            Button(
                text=Format('{btn_age_reset}'),
                id='btn_age_reset',
                on_click=btn_age_reset_click
            ),
            Button(
                text=Format('{btn_age_clear}'),
                id='btn_age_clear',
                on_click=btn_age_clear_click
            ),
            Button(
                text=Format('{btn_age_cancel}'),
                id='btn_age_cancel',
                on_click=btn_age_cancel_click
            ),
        ),
        getter=get_age,
        state=Aboutme.age,
    ),

    # Пол
    Window(
        Format("{win_gender}"),
        Row(
            Radio(
                checked_text=Format('[✔ {item[0]} ]'),
                unchecked_text=Format('[ {item[0]} ]'),
                id='gender',
                item_id_getter=operator.itemgetter(1),
                items='radio_gender',
            ),
        ),
        Row(
            SwitchTo(
                text=Format('{btn_gender_ok}'),
                id='btn_gender_ok',
                state=Aboutme.profile),
            Button(
                text=Format('{btn_gender_reset}'),
                id='btn_gender_reset',
                on_click=btn_gender_reset_click
            ),
            Button(
                text=Format('{btn_gender_clear}'),
                id='btn_gender_clear',
                on_click=btn_gender_clear_click
            ),
            Button(
                text=Format('{btn_gender_cancel}'),
                id='btn_gender_cancel',
                on_click=btn_gender_cancel_click
            ),
        ),
        getter=get_gender,
        state=Aboutme.gender,
    ),

    # Состояние
    Window(
        Format("<b>{win_status_h}</b>\n"),
        Format("<b>{txt_status}</b>\n"),
        Format("{win_status_txt}\n"),
        TextInput(
            id="status_text",
            type_factory=inp_status_check,
            on_success=inp_status_success,
            on_error=inp_age_error,
        ),
        Row(
            SwitchTo(
                text=Format('{btn_status_ok}'),
                id='btn_status_ok',
                state=Aboutme.profile),
            Button(
                text=Format('{btn_status_reset}'),
                id='btn_status_reset',
                on_click=btn_status_reset_click
            ),
            Button(
                text=Format('{btn_status_clear}'),
                id='btn_status_clear',
                on_click=btn_status_clear_click
            ),
            Button(
                text=Format('{btn_status_cancel}'),
                id='btn_status_cancel',
                on_click=btn_status_cancel_click
            ),
        ),
        getter=get_status,
        state=Aboutme.status,
    ),

    # Оценка состояния
    Window(
        Format("{win_grade}"),
        Group(
            Row(
                Radio(
                    checked_text=Format('✔ {item[0]}'),
                    unchecked_text=Format('{item[0]}'),
                    id='grade',
                    item_id_getter=operator.itemgetter(1),
                    items='radio_grade'
                ),
            ),
            width=5
        ),
        Row(
            SwitchTo(
                text=Format('{btn_grade_ok}'),
                id='btn_grade_ok',
                state=Aboutme.profile),
            Button(
                text=Format('{btn_grade_reset}'),
                id='btn_grade_reset',
                on_click=btn_grade_reset_click
            ),
            Button(
                text=Format('{btn_grade_clear}'),
                id='btn_grade_clear',
                on_click=btn_grade_clear_click
            ),
            Button(
                text=Format('{btn_grade_cancel}'),
                id='btn_grade_cancel',
                on_click=btn_grade_cancel_click
            ),
        ),
        getter=get_grade,
        state=Aboutme.grade,
    ),
)
