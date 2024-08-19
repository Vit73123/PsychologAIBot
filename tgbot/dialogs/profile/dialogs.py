from aiogram.types import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format

from tgbot.dialogs.states import Profile
from .getters import get_start

profile_dialog = Dialog(
    Window(
        Format('{dlg_profile}'),
        StaticMedia(
            path='resources/images/profile.jpg',
            type=ContentType.PHOTO
        ),
        getter=get_start,
        state=Profile.start,
    )
)
