import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Radio
from aiogram_dialog.widgets.text import Const, Format

from tests.dialogs.states import *
from .callbacks import *
from .getters import *

start_dialog = Dialog(

    # Start
    Window(
        Const("Начать сеанс с психологом"),
        TextInput(
            id="inp_test",
            type_factory=inp_test_check,
            # on_success=inp_test_success,
        ),
        Row(
            Radio(
                checked_text=Format('[✔ {item[0]} ]'),
                unchecked_text=Format('[ {item[0]} ]'),
                id='radio_test',
                item_id_getter=operator.itemgetter(1),
                items='radio_test',
            ),
        ),
        Button(
            text=Const("Поверить значение"),
            id='btn_test_check',
            on_click=btn_test_check_click
        ),
        Button(
            text=Const("Установить значение"),
            id='btn_test_set',
            on_click=btn_test_set_click
        ),
        Button(
            text=Const("Удалить виджет"),
            id='btn_test_remove',
            on_click=btn_test_remove_click
        ),
        Button(
            text=Const("Проверить репозиторий"),
            id='btn_test_repo',
            on_click=btn_test_repo_click
        ),
        # SwitchTo(
        #     text=Const("Начать сеанс"),
        #     id='btn_psychology_start',
        #     state=states.Start.psychology,
        # ),
        getter=get_start,
        state=Start.start,
    ),

    Window(
        Const("bbb"),
        SwitchTo(
            text=Const("Завершить сеанс"),
            id='btn_psychology_stop',
            state=Start.start,
        ),
        getter=get_psychology,
        state=Start.psychology,
    ),
)
