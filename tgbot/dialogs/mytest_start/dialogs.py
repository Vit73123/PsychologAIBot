from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

# from .callbacks import *
from .getters import *

mytest_start_dialog = Dialog(

    # Мой тест
    Window(
        Const('<b>Мой тест</b>'),
        StaticMedia(
            path='resources/images/profile_psycho.jpg',
            type=ContentType.PHOTO
        ),
        getter=get_mytest,
        state=MyTest.start,
    ),
)
