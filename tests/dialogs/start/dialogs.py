from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Const

from tests.dialogs import states
from .getters import *

start_dialog = Dialog(

    # Start
    Window(
        Const("Начать сеанс с психологом"),
        SwitchTo(
            text=Const("Начать сеанс"),
            id='btn_psychology_start',
            state=states.Start.psychology,
        ),
        getter=get_start,
        state=states.Start.start,
    ),

    Window(
        Const("bbb"),
        SwitchTo(
            text=Const("Завершить сеанс"),
            id='btn_psychology_stop',
            state=states.Start.start,
        ),
        getter=get_psychology,
        state=states.Start.psychology,
    ),
)
