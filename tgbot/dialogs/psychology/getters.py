from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner


async def get_start(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_psychology_start": i18n.win.psychology.start(),
        "btn_psychology_start_session": i18n.btn.psychology.start.session(),
        "btn_back": i18n.btn.back(),
    }
