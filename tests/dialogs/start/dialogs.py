from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format

from tests.dialogs import states
from .callbacks import *
from .getters import *

start_dialog = Dialog(

    # Start
    Window(
        Const('<b>Start</b>'),
        # Format("<b>{{html.quote(user[name])}}</b>"),
        Format("<b>{user[name]}</b>"),
        StaticMedia(
            path='resources/images/profile_psycho.jpg',
            type=ContentType.PHOTO
        ),
        Button(Const('Вперёд'), id='next', on_click=btn_dialog1_click),
        getter=get_start,
        state=states.Start.start,
    ),
)
