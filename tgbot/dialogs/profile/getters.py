from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner


# О себе
async def get_aboutme(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_aboutme": i18n.win.aboutme(),
        "btn_aboutme_profile": i18n.btn.aboutme.profile(),
        "btn_aboutme_back": i18n.btn.back(),
    }


# Профиль
async def get_profile(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    gender = [
        (i18n.btn.aboutme.profile.mail(), '1'),
        (i18n.btn.aboutme.profile.femail(), '2'),
    ]
    return {
        "win_aboutme_profile_h_state": i18n.win.aboutme.profile.h.state(),
        "win_aboutme_profile_h_grade": i18n.win.aboutme.profile.h.grade(),
        "btn_aboutme_profile_name": i18n.btn.aboutme.profile.name(),
        "btn_aboutme_profile_age": i18n.btn.aboutme.profile.age(),
        "btn_aboutme_profile_state": i18n.btn.aboutme.profile.state(),
        "btn_aboutme_profile_save": i18n.btn.save(),
        "btn_aboutme_profile_back": i18n.btn.back(),
        "radio_aboutme_profile_gender": gender,
    }


# Имя
async def get_name(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_aboutme_profile_name": i18n.win.aboutme.profile.name(),
        "btn_aboutme_profile_name_skip": i18n.btn.skip(),
    }


# Возраст
async def get_age(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_aboutme_profile_age": i18n.win.aboutme.profile.age(),
        "btn_aboutme_profile_age_skip": i18n.btn.skip(),
    }


# Состояние
async def get_state(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_aboutme_profile_state": i18n.win.aboutme.profile.state(),
        "btn_aboutme_profile_state_skip": i18n.btn.skip(),
        "btn_aboutme_profile_state_back": i18n.btn.back(),
    }


# Оценка состояния
async def get_grade(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    grades = [("+1 😏", '1'), ("+2 😌", '2'), ("+3 🙂", '3'), ("+4 😀", '4'), ("+5 😆", '5'),
              ("-1 🫤", '6'), ("-2 🙁", '7'), ("-3 😟", '8'), ("-4 😧", '9'), ("-5 🥵", '10'),
              ("😑 Мне всё безразлично", 11)]
    return {
        "win_aboutme_profile_grade": i18n.win.aboutme.profile.grade(),
        "btn_aboutme_profile_grade_skip": i18n.btn.skip(),
        "btn_aboutme_profile_grade_back": i18n.btn.back(),
        "radio_aboutme_profile_grades": grades,
    }
