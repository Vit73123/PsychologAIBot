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
        "win_profile_start": i18n.win.profile.start(),
        "btn_profile_start_aboutme": i18n.btn.profile.start.aboutme(),
        "btn_back": i18n.btn.back(),
    }


async def get_aboutme(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_profile_aboutme": i18n.win.profile.aboutme(),
        "btn_profile_aboutme_name": i18n.btn.profile.aboutme.name(),
        "btn_profile_aboutme_male": i18n.btn.profile.aboutme.mail(),
        "btn_profile_aboutme_female": i18n.btn.profile.aboutme.femail(),
        "btn_profile_aboutme_age": i18n.btn.profile.aboutme.age(),
        "btn_profile_aboutme_status": i18n.btn.profile.aboutme.status(),
        "btn_ok": i18n.btn.ok(),
        "btn_cancel": i18n.btn.cancel(),
    }
