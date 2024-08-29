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
        "win_tests_start": i18n.win.tests.start(),
        "btn_tests_start_choosetest": i18n.btn.tests.start.choosetest(),
        "btn_back": i18n.btn.back(),
    }
