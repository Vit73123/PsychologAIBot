from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Tests
from .callbacks import (
    btn_choose_test_clicked,
    btn_back_clicked,
)
from .getters import get_start

tests_dialog = Dialog(
    Window(
        Format('{dlg_tests}'),
        StaticMedia(
            path='resources/images/tests.jpg',
            type=ContentType.PHOTO
        ),
        Row(
            Button(
                text=Format('{btn_choose_test}'),
                id='btn_choose_test',
                on_click=btn_choose_test_clicked,
            ),
            Button(
                text=Format('{btn_back}'),
                id='btn_back',
                on_click=btn_back_clicked,
            ),
        ),
        getter=get_start,
        state=Tests.start,
    )
)
