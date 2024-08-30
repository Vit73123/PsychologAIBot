import operator

from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Row, Radio, Group
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format, Const

from .callbacks import *
from .getters import *

profile_dialog = Dialog(

    # О себе
    Window(
        Format('{win_aboutme}'),
        StaticMedia(
            path='resources/images/profile.jpg',
            type=ContentType.PHOTO
        ),
        Row(
            Button(
                text=Format('{btn_aboutme_profile}'),
                id='btn_aboutme_profile',
                on_click=btn_aboutme_profile_clicked,
            ),
            Button(
                text=Format('{btn_aboutme_back}'),
                id='btn_aboutme_back',
                on_click=btn_aboutme_back_clicked,
            ),
        ),
        getter=get_aboutme,
        state=Aboutme.start,
    ),

    # Профиль
    Window(
        Format('{win_aboutme_profile_h_state}'),
        Format(
            'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis quo ratione, adipisci ducimus commodi eligendi dolorum maxime molestias ad debitis architecto cumque molestiae numquam, aperiam qui odit perferendis repellat velit!'
        ),
        Format('\n{win_aboutme_profile_h_grade}'),
        Format(
            '+3 🙂'
        ),
        Row(
            Button(
                text=Format('{btn_aboutme_profile_name}'),
                id='btn_aboutme_profile_name',
                on_click=btn_aboutme_profile_name_clicked,
            ),
        ),
        Row(
            Radio(
                checked_text=Format('[✔ {item[0]} ]'),
                unchecked_text=Format('[ {item[0]} ]'),
                id='radio_aboutme_profile_gender',
                item_id_getter=operator.itemgetter(1),
                items='radio_aboutme_profile_gender'
            ),
            Button(
                text=Format('{btn_aboutme_profile_age}'),
                id='btn_aboutme_profile_age',
                on_click=btn_aboutme_profile_age_clicked,
            ),
        ),
        Row(
            Button(
                text=Format('{btn_aboutme_profile_state}'),
                id='btn_aboutme_profile_state',
                on_click=btn_aboutme_profile_state_clicked,
            ),
        ),
        Row(
            Button(
                text=Format('{btn_aboutme_profile_save}'),
                id='btn_aboutme_profile_save',
                on_click=btn_aboutme_profile_save_clicked,
            ),
            Button(
                text=Format('{btn_aboutme_profile_back}'),
                id='btn_aboutme_profile_back',
                on_click=btn_aboutme_profile_back_clicked,
            ),
        ),
        getter=get_profile,
        state=Aboutme.profile,
    ),

    # Имя:
    Window(
        Format("{win_aboutme_profile_name}"),
        TextInput(
            id="inp_aboutme_profile_name",
            type_factory=inp_name_check,
            on_success=inp_name_success,
            on_error=inp_name_error,
        ),
        Row(
            Button(
                text=Format('{btn_aboutme_profile_name_skip}'),
                id='btn_aboutme_profile_name_skip',
                on_click=btn_aboutme_profile_name_skip_clicked,
            ),
        ),
        getter=get_name,
        state=Aboutme.name,
    ),

    # Возраст:
    Window(
        Format("{win_aboutme_profile_age}"),
        TextInput(
            id="inp_aboutme_profile_age",
            type_factory=inp_age_check,
            on_success=inp_age_success,
            on_error=inp_age_error,
        ),
        Row(
            Button(
                text=Format('{btn_aboutme_profile_age_skip}'),
                id='btn_aboutme_profile_age_skip',
                on_click=btn_aboutme_profile_age_skip_clicked,
            ),
        ),
        getter=get_name,
        state=Aboutme.age,
    ),

    # Состояние
    Window(
        Format("{win_aboutme_profile_state}"),
        TextInput(
            id="inp_aboutme_profile_state",
            type_factory=inp_state_check,
            on_success=inp_state_success,
            on_error=inp_age_error,
        ),
        Row(
            Button(
                text=Format('{btn_aboutme_profile_state_skip}'),
                id='btn_aboutme_profile_state_skip',
                on_click=btn_aboutme_profile_state_skip_clicked,
            ),
            Button(
                text=Format('{btn_aboutme_profile_state_back}'),
                id='btn_aboutme_profile_state_back',
                on_click=btn_aboutme_profile_state_back_clicked,
            ),
        ),
        getter=get_state,
        state=Aboutme.state,
    ),

    # Оценка состояния
    Window(
        Const("{win-aboutme-profile-grade}}"),
        Group(
            Row(
                Radio(
                    checked_text=Format('✔ {item[0]}'),
                    unchecked_text=Format('{item[0]}'),
                    id='radio_aboutme_profile_grades',
                    item_id_getter=operator.itemgetter(1),
                    items='radio_aboutme_profile_grades'
                ),
            ),
            width=5
        ),
        Row(
            Button(
                text=Format('{btn_aboutme_profile_grade_skip}'),
                id='btn_aboutme_profile_grade_skip',
                on_click=btn_aboutme_profile_grade_skip_clicked,
            ),
            Button(
                text=Format('{btn_aboutme_profile_grade_back}'),
                id='btn_aboutme_profile_grade_back',
                on_click=btn_aboutme_profile_grade_back_clicked,
            ),
        ),
        getter=get_grade,
        state=Aboutme.grade,
    ),
)
