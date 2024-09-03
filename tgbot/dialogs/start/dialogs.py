from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Row
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format, Const

from tgbot.dialogs import states
from .getters import get_start

start_dialog = Dialog(
    Window(
        Format('{win_start}'),
        StaticMedia(
            path='resources/images/start.png',
            type=ContentType.PHOTO
        ),
        Start(Format('{btn_psychology}'), id='btn_psychology', state=states.Psychology.start),
        Start(Format('{btn_tests}'), id='btn_tests', state=states.Tests.start),
        Start(Format('{btn_aboutme}'), id='btn_aboutme', state=states.Aboutme.start),
        getter=get_start,
        state=states.Start.start,
    )
)
