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
        "dlg_tests": i18n.dlg.tests(),
        "btn_choose_test": i18n.btn.choose.test(),
        "btn_back": i18n.btn.back(),
    }
