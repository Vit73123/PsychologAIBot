from logging import getLogger
from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.config import Config
from tgbot.db import Repo
from tgbot.db.dao import UserDAO, StatusDAO
from tgbot.tools.logger import get_logger_dev
from tgbot.utils import create_aboutme_string, load_status_grades, get_grade_string

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
    log.debug(" About me: get_aboutme: context: %s", dialog_manager.current_context())

    user: UserDAO = await repo.user.get(dialog_manager.start_data['user']['id'])
    user_upd: UserDAO = UserDAO(user.id)
    dialog_manager.dialog_data.update({'user': user, 'user_upd': user_upd})

    return {
        "win_aboutme": i18n.win.aboutme(),
        "btn_aboutme_profile": i18n.btn.aboutme.profile(),
        "btn_aboutme_getback_home": i18n.btn.getback.home(),
    }


# Профиль
async def get_profile(
        dialog_manager: DialogManager,
        repo: Repo,
        config: Config,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Profile: get_profile: context: %s", dialog_manager.current_context())

    user: UserDAO = dialog_manager.dialog_data.get('user')
    user_upd: UserDAO = dialog_manager.dialog_data.get('user_upd')

    aboutme_txt = create_aboutme_string(user=user, user_upd=user_upd, i18n=i18n)

    status: StatusDAO = await repo.status.get_last_by_user_id(user.id)
    status_upd = StatusDAO(status.id)

    status_txt = status.text if not status_upd.text else status.text

    status_grades: dict = load_status_grades(config.root_path / 'resources' / 'emoji')
    dialog_manager.dialog_data.update({'status_grades': status_grades})

    log_dev.debug(" Profile: get_profile: context: %s", dialog_manager.current_context())

    grade_txt = get_grade_string(status.grade, status_grades) if not status_upd.grade else get_grade_string(
        status_upd.grade, status_grades)

    log_dev.debug(" Profile: grade_txt %s", grade_txt)

    return {
        "win_profile_aboutme": aboutme_txt,
        "win_profile_h_status": i18n.win.aboutme.profile.h.status(),
        "win_profile_status": status_txt,
        "win_profile_h_grade": i18n.win.aboutme.profile.h.grade(),
        "win_profile_grade": grade_txt,
        "btn_profile_name": i18n.btn.aboutme.profile.name(),
        "btn_profile_age": i18n.btn.aboutme.profile.age(),
        "btn_profile_gender": i18n.btn.aboutme.profile.gender(),
        "btn_profile_status": i18n.btn.aboutme.profile.status(),
        "btn_profile_grade": i18n.btn.aboutme.profile.grade(),
        "btn_profile_ok": i18n.btn.ok(),
        "btn_profile_setback": i18n.btn.setback(),
        "btn_profile_clear": i18n.btn.clear(),
        "btn_profile_getback": i18n.btn.getback(),
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
async def get_status(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_status": i18n.win.aboutme.profile.status(),
        "btn_status_skip": i18n.btn.skip(),
        "btn_status_back": i18n.btn.back(),
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
