from logging import getLogger
from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Radio
from fluentogram import TranslatorRunner

from tgbot.db.models.user import Gender
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner


# Пол
async def get_gender(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    gender = [
        (i18n.btn.aboutme.profile.gender.male(), '1'),
        (i18n.btn.aboutme.profile.gender.female(), '2'),
    ]
    widget_data = dialog_manager.current_context().widget_data
    dialog_data = dialog_manager.dialog_data

    updated = 'radio_gender' in widget_data
    radio_gender = dialog_manager.find('radio_gender') if updated else None


    check_radio(1, dialog_manager)

    radio: Radio = dialog_manager.find('radio_gender')
    text = radio.get_checked()
    gender_enum: Gender = text

    check_radio(2, dialog_manager)

    return {
        "win_gender": i18n.win.aboutme.profile.gender(),
        "win_gender_text": text,
        "win_gender_enum": gender_enum,
        "radio_gender": gender,
        "btn_gender_clear": i18n.btn.clear(),
        "btn_gender_cancel": i18n.btn.cancel(),
    }

def check_radio(index: int, dialog_manager: DialogManager):
    context = dialog_manager.current_context()

    log_dev.debug(" (%d) context: %s", index, context)
    log_dev.debug(" (%d) context: %s", index, context.widget_data)
    log_dev.debug(" radio_gender exists: %s", 'radio_gender' in context.widget_data)

    radio_gender: Radio = dialog_manager.find('radio_gender')

    log_dev.debug(" radio_gender id: %s", radio_gender.get_checked())
    log_dev.debug(" radio_gender exists: %s", 'radio_gender' in context.widget_data)

    context.widget_data.pop('radio_gender')

    log_dev.debug(" radio_gender exists: %s", 'radio_gender' in context.widget_data)
    log_dev.debug(" (%d) context: %s\n", index, dialog_manager.current_context())
