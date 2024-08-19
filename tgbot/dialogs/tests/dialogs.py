from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Tests
from .getters import get_start

tests_dialog = Dialog(
    Window(
        Format('{dlg_tests}'),
        StaticMedia(
            path='resources/images/tests.jpg',
            type=ContentType.PHOTO
        ),
        getter=get_start,
        state=Tests.start,
    )
)
