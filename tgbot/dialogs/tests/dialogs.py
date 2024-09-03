from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Cancel
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Tests
from .callbacks import (
    btn_start_dotest_clicked,
)
from .getters import get_start

# Тесты
tests_dialog = Dialog(
    Window(
        Format('{win_tests}'),
        StaticMedia(
            path='resources/images/tests.jpg',
            type=ContentType.PHOTO
        ),
        Button(
            text=Format('{btn_tests_start_dotest}'),
            id='btn_start_dotest',
            on_click=btn_start_dotest_clicked,
        ),
        Cancel(Format('{btn_back_start}'), id='btn_back_start'),
        getter=get_start,
        state=Tests.start,
    )
)
