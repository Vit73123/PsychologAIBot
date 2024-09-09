import operator

from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Row, Group, Cancel, Back, SwitchTo
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format, Const

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
        Cancel(Format('{btn_aboutme_getback_home}'), id='btn_aboutme_getback_home'),
        getter=get_aboutme,
        state=Aboutme.start,
    ),

    # Профиль
    Window(

        Format('{win_profile_aboutme}\n'),
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
            Back(Format('{btn_profile_cancel}'), id='btn_profile_cancel'),
        ),
        getter=get_profile,
        state=Aboutme.profile,
    ),

    # Имя
    Window(
        Format("{win_name}\n"),
        TextInput(
            id="name",
            type_factory=inp_name_check,
            on_success=inp_name_success,
            on_error=inp_name_error,
        ),
        Row(
            Button(
                text=Format('{btn_name_ok}'),
                id='btn_name_ok',
                on_click=btn_name_ok_click
            ),
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
        Format("{win_age}"),
        TextInput(
            id="age",
            type_factory=inp_age_check,
            on_success=inp_age_success,
            on_error=inp_age_error,
        ),
        Row(
            Button(
                text=Format('{btn_age_ok}'),
                id='btn_age_ok',
                on_click=btn_age_ok_click
            ),
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
            SwitchTo(
                text=Format('{btn_age_cancel}'),
                id='btn_age_cancel',
                state=Aboutme.profile
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
            Button(
                text=Format('{btn_gender_ok}'),
                id='btn_gender_ok',
                on_click=btn_gender_ok_click
            ),
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
            SwitchTo(
                text=Format('{btn_gender_cancel}'),
                id='btn_gender_cancel',
                state=Aboutme.profile
            ),
        ),
        getter=get_gender,
        state=Aboutme.gender,
    ),

    # Состояние
    Window(
        Format("{win_status}"),
        TextInput(
            id="status_text",
            type_factory=inp_status_check,
            on_success=inp_status_success,
            on_error=inp_age_error,
        ),
        Row(
            Button(
                text=Format('{btn_status_ok}'),
                id='btn_status_ok',
                on_click=btn_status_ok_click
            ),
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
            SwitchTo(
                text=Format('{btn_status_cancel}'),
                id='btn_status_cancel',
                state=Aboutme.profile
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
            Button(
                text=Format('{btn_grade_ok}'),
                id='btn_grade_ok',
                on_click=btn_grade_ok_click
            ),
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
            SwitchTo(
                text=Format('{btn_grade_cancel}'),
                id='btn_grade_cancel',
                state=Aboutme.profile
            ),
        ),
        getter=get_grade,
        state=Aboutme.grade,
    ),

    # Да/Нет Имя
    Window(
        Format("{win_yesno_name}"),
        Row(
            SwitchTo(
                text=Format('{btn_yesno_name_yes}'),
                id='btn_yesno_name_yes',
                state=Aboutme.profile
            ),
            Button(
                text=Format('{btn_yesno_name_no}'),
                id='btn_yesno_name_no',
                on_click=btn_grade_reset_click
            ),
        ),
        getter=get_yesno_name,
        state=Aboutme.yesno_name,
    ),
)
