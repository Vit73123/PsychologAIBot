from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

# from .callbacks import *
from .getters import *

mytest_1_dialog = Dialog(

    # Мой тест
    Window(
        Const('<b>My test 1</b>'),
        getter=get_mytest,
        state=MyTest1.start,
    ),
)
