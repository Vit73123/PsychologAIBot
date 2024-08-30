from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from tests.dialogs import states
# from .callbacks import *
from .getters import *

start_dialog = Dialog(

    # Start
    Window(
        Const('<b>Start</b>'),
        StaticMedia(
            path='resources/images/profile_psycho.jpg',
            type=ContentType.PHOTO
        ),
        Start(Const('Вперёд'), id='next', state=states.Dialog_1.dialog_1),
        getter=get_start,
        state=states.Start.start,
    ),
)
