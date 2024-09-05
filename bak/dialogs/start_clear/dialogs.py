import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.text import Format, Const

from tests.dialogs import states
from .callbacks import *
from .getters import *

start_dialog = Dialog(

    # Start
    Window(
        # Format("{win_gender}"),
        # Format("{win_gender_text}"),
        # Format("{win_gender_enum}"),
        # Row(
        #     Radio(
        #         checked_text=Format('✔ {item[0]}'),
        #         unchecked_text=Format('  {item[0]}'),
        #         id='radio_gender',
        #         item_id_getter=operator.itemgetter(1),
        #         items='radio_gender',
        #     ),
        # ),
        # Row(
        #     Button(
        #         text=Format('{btn_gender_clear}'),
        #         id='btn_gender_clear',
        #         on_click=btn_gender_clear_clicked
        #     ),
        # ),
        Const("Add / Clear"),
        Row(
            Button(
                text=Const('Add Widget'),
                id='btn_add_widget',
                on_click=btn_add_widget_clicked
            ),
            Button(
                text=Const('Add Dialog'),
                id='btn_add_dialog',
                on_click=btn_add_dialog_clicked
            ),
            Button(
                text=Const('Add to All Dialogs'),
                id='btn_add_all_dialog',
                on_click=btn_add_all_dialog_clicked
            ),
        ),
        Row(
            Button(
                text=Const('Clear Widgets'),
                id='btn_widget_clear',
                on_click=btn_widget_clear_clicked
            ),
            Button(
                text=Const('Clear Dialog'),
                id='btn_dialog_clear',
                on_click=btn_dialog_clear_clicked
            ),
            Button(
                text=Const('Clear All Dialogs'),
                id='btn_all_dialog_clear',
                on_click=btn_all_dialog_clear_clicked
            ),
        ),
        getter=get_gender,
        state=states.Start.start,
    ),
)
