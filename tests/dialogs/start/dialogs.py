from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from tests.dialogs import states
from .getters import *

start_dialog = Dialog(

    # Start
    Window(
        # Format("{emoji-home}"),
        # Format("{btn-home}"),
        # Format("{btn-getback-home}"),

        # Format("{emoji-pin}"),
        # Format("{win-start}"),
        # Format("{win-aboutme}"),

        # Format("{emoji-next}"),
        # Format("{emoji-back}"),

        # Format("{emoji-skip}"),
        # Format("{emoji-clear}"),
        # Format("{emoji-getback}"),
        # Format("{emoji-setback}"),
        # Format("{emoji-save}"),
        # Format("{emoji-ok}"),
        # Format("{emoji-cancel}"),
        # Format("{emoji-i-hi}"),
        # Format("{emoji-i-profile}"),
        # Format("{emoji-i-am}"),

        # Format("{emoji-i-wrong}"),
        # Format("{emoji-i-oh}"),
        # Format("{emoji-male}"),
        # Format("{emoji-female}"),

        #         "emoji-me-important": i18n.emoji.me.important(),
        #         "emoji-grade": i18n.emoji.grade(),
        #         "emoji-psychologist-man": i18n.emoji.psychologist.man(),
        #         "emoji-psychologist-woman": i18n.emoji.psychologist.woman(),

        Format("{emoji-me-important}"),
        Format("{emoji-grade}"),
        Format("{emoji-psychologist-man}"),
        Format("{emoji-psychologist-woman}"),

        # StaticMedia(
        #     path='resources/images/profile_psycho.jpg',
        #     type=ContentType.PHOTO
        # ),
        # Button(Const('Вперёд'), id='next', on_click=btn_dialog1_click),
        getter=get_start,
        state=states.Start.start,
    ),
)
