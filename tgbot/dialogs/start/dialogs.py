from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs import states
from .callbacks import *
from .getters import get_start

# Старт
start_dialog = Dialog(
    Window(
        Format('<b>Дорогой друг, {user_name}!</b>'),
        Format('{win_start}'),
        StaticMedia(
            path='resources/images/start.png',
            type=ContentType.PHOTO
        ),
        Row(
            Button(Format('{btn_psychology}'), id='btn_psychology', on_click=btn_psychology_click),
            Button(Format('{btn_tests}'), id='btn_tests', on_click=btn_tests_click),
        ),
        Button(Format('{btn_aboutme}'), id='btn_aboutme', on_click=btn_aboutme_click),
        getter=get_start,
        state=states.Start.start,
    )
)
