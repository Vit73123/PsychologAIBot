from logging import getLogger
from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.db import Repo
from tgbot.db.dao import UserDAO
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner


# О себе
async def get_aboutme(
        dialog_manager: DialogManager,
        repo: Repo,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" About me: get_aboutme: context: %s", dialog_manager.current_context())

    user: UserDAO = await repo.user.get(
        dialog_manager.start_data['user']['id']
    )

    print(user)

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
        "win_profile_h_state": i18n.win.aboutme.profile.h.state(),
        "win_profile_h_grade": i18n.win.aboutme.profile.h.grade(),
        "btn_profile_name": i18n.btn.aboutme.profile.name(),
        "btn_profile_age": i18n.btn.aboutme.profile.age(),
        "btn_profile_state": i18n.btn.aboutme.profile.state(),
        "btn_profile_save": i18n.btn.save(),
        "btn_profile_back": i18n.btn.back(),
        "radio_gender": gender,
    }


# Имя
async def get_name(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_name": i18n.win.aboutme.profile.name(),
        "btn_name_skip": i18n.btn.skip(),
    }


# Возраст
async def get_age(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_age": i18n.win.aboutme.profile.age(),
        "btn_age_skip": i18n.btn.skip(),
    }


# Состояние
async def get_state(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_state": i18n.win.aboutme.profile.state(),
        "btn_state_skip": i18n.btn.skip(),
        "btn_state_back": i18n.btn.back(),
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
        "win_grade": i18n.win.aboutme.profile.grade(),
        "btn_grade_skip": i18n.btn.skip(),
        "btn_grade_back": i18n.btn.back(),
        "radio_grade": grades,
    }
