from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel, SwitchTo, Next, Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format, Const

from .callbacks import *
from .getters import *

psychology_dialog = Dialog(

    # Психология
    Window(
        Format('{win_psychology}'),
        StaticMedia(
            path='resources/images/psychology.jpg',
            type=ContentType.PHOTO
        ),
        Next(Format('{btn_appointment_start}'), id='btn_appointment_start'),
        Cancel(Format('{btn_getback_home}'), id='btn_getback_home'),
        getter=get_psychology,
        state=Psychology.start,
    ),

    # GPT
    Window(
        Format("{gpt_message}"),
        TextInput(
            id="inp_message",
            type_factory=inp_message_check,
            on_success=inp_message_success,
        ),
        Button(
            text=Format("{btn_appointment_stop}"),
            id='btn_appointment_stop',
            on_click=btn_appointment_stop,
        ),
        getter=get_appointment,
        state=Psychology.appointment,
    ),

    # Ревью
    Window(
        Format("{gpt_message}"),
        SwitchTo(
            text=Format("{btn_appointment_thankyou}"),
            id='btn_appointment_thankyou',
            state=Psychology.start,
        ),
        getter=get_review,
        state=Psychology.review,
    ),
)
