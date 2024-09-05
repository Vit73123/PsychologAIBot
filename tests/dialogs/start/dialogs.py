import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Radio
from aiogram_dialog.widgets.text import Format

from tests.dialogs import states
from .callbacks import *
from .getters import *

start_dialog = Dialog(

    # Start
    Window(
        Format("{win_gender}"),
        Format("{win_gender_text}"),
        Format("{win_gender_enum}"),
        Row(
            Radio(
                checked_text=Format('✔ {item[0]}'),
                unchecked_text=Format('  {item[0]}'),
                id='radio_gender',
                item_id_getter=operator.itemgetter(1),
                items='radio_gender',
            ),
        ),
        Row(
            Button(
                text=Format('{btn_gender_clear}'),
                id='btn_gender_clear',
                on_click=btn_gender_clear_clicked
            ),
        ),
        getter=get_gender,
        state=states.Start.start,
    ),
)
