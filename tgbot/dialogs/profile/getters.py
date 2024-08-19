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
        "dlg_profile": i18n.dlg.profile(),
        "btn_create_profile": i18n.btn.create.profile(),
        "btn_back": i18n.btn.back(),
    }
