from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const

from tests.dialogs import states
# from .callbacks import *
from .getters import *

dialog_1_dialog = Dialog(

    # Диалог 1
    Window(
        Const('<b>Диалог 1</b>'),
        Cancel(Const('Назад'), id='back'),
        getter=get_dialog_1,
        state=states.Dialog_1.start,
    ),
)
