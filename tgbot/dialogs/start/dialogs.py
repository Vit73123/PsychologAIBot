from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start
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
        Start(Const('Вперёд'), id='next', state=states.Aboutme.start),
        getter=get_start,
        state=states.Start.start,
    )
)
