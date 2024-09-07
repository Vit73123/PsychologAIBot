from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.db import Repo
from tgbot.db.dao import StatusDAO, UserDAO
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.dialogs import create_aboutme_text, create_status_text, create_grade_text, create_name_text

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner


# О себе
async def get_aboutme(
        dialog_manager: DialogManager,
        state: FSMContext,
        repo: Repo,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Aboutme: get_aboutme: context: %s", dialog_manager.current_context())
    log_dev.debug(" Aboutme: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    return {
        "win_aboutme": i18n.win.aboutme(),
        "btn_aboutme_profile": i18n.btn.aboutme.profile(),
        "btn_aboutme_getback_home": i18n.btn.getback.home(),
    }


# Профиль
async def get_profile(
        dialog_manager: DialogManager,
        state: FSMContext,
        repo: Repo,
        grades: dict,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Profile: get_profile: context: %s", dialog_manager.current_context())
    log_dev.debug(" Profile: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    state_data = await state.get_data()

    # Добавляем пользователя в контекст FSM, если его ещё там нет (ленивая загрузка из базы данных)
    if 'user' not in state_data:
        user: UserDAO = await repo.user.get(dialog_manager.start_data['user_id'])
        await state.update_data({'user': user})
        dialog_manager.dialog_data.update({'updated_items': set()})
    # Берём пользователя из контекста FSM, если он уже там есть
    else:
        user: UserDAO = state_data['user']

    # Добавляем состояние пользователя в контекст FSM, если его ещё там нет (ленивая загрузка из базы данных)
    if 'status' not in state_data:
        status: StatusDAO = await repo.status.get_last_by_user_id(dialog_manager.start_data['user_id'])
        status_data = {'status': status}
        state_data.update(status_data)
        await state.update_data(status_data)
    # Берём состояние пользователя из контекста FSM, если оно уже там есть
    else:
        status: StatusDAO = state_data['status']

    # Создаём строку описания пользователя - первая строка с данными пользователя в свободном стиле
    aboutme_txt = create_aboutme_text(user=user, dialog_manager=dialog_manager, i18n=i18n)
    status_txt = create_status_text(status=status, dialog_manager=dialog_manager)
    grade_txt = create_grade_text(status=status, dialog_manager=dialog_manager, grades=grades)

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
        "btn_profile_cancel": i18n.btn.cancel.getback(),
    }


# Имя
async def get_name(
        state: FSMContext,
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Name: get_name: context: %s", dialog_manager.current_context())
    log_dev.debug(" Name: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    state_data = await state.get_data()
    user: UserDAO = state_data['user']
    name_txt: str = create_name_text(user, dialog_manager, i18n)

    return {
        "win_name_h": name_txt,
        "win_name_txt": i18n.win.aboutme.name.txt(),
        "btn_name_setback": i18n.btn.setback(),
        "btn_name_clear": i18n.btn.clear(),
        "btn_name_cancel": i18n.btn.cancel.getback(),
    }


# Возраст
async def get_age(
        dialog_manager: DialogManager,
        state: FSMContext,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Age: get_age: context: %s", dialog_manager.current_context())
    log_dev.debug(" Age: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    return {
        "win_age": i18n.win.aboutme.profile.age(),
        "btn_age_setback": i18n.btn.setback(),
        "btn_age_clear": i18n.btn.clear(),
        "btn_age_cancel": i18n.btn.cancel.getback(),
    }


# Пол
async def get_gender(
        dialog_manager: DialogManager,
        state: FSMContext,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Gender: get_gender: context: %s", dialog_manager.current_context())
    log_dev.debug(" Gender: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    gender = [
        (i18n.btn.aboutme.profile.gender.male(), '1'),
        (i18n.btn.aboutme.profile.gender.female(), '2'),
    ]
    return {
        "win_gender": i18n.win.aboutme.profile.gender(),
        "radio_gender": gender,
        "btn_gender_ok": i18n.btn.ok(),
        "btn_gender_clear": i18n.btn.clear(),
        "btn_gender_cancel": i18n.btn.cancel(),
    }


# Состояние
async def get_status(
        dialog_manager: DialogManager,
        state: FSMContext,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Status: get_status: context: %s", dialog_manager.current_context())
    log_dev.debug(" Status: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    return {
        "win_status": i18n.win.aboutme.profile.status(),
        "btn_status_setback": i18n.btn.setback(),
        "btn_status_clear": i18n.btn.clear(),
        "btn_status_cancel": i18n.btn.cancel(),
    }


# Оценка состояния
async def get_grade(
        dialog_manager: DialogManager,
        state: FSMContext,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Grade: get_grade: context: %s", dialog_manager.current_context())
    log_dev.debug(" Grade: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    grades = [("+1 😏", '1'), ("+2 😌", '2'), ("+3 🙂", '3'), ("+4 😀", '4'), ("+5 😆", '5'),
              ("-1 🫤", '6'), ("-2 🙁", '7'), ("-3 😟", '8'), ("-4 😧", '9'), ("-5 🥵", '10'),
              ("😑 Мне всё безразлично", 11)]
    return {
        "win_grade": i18n.win.aboutme.profile.grade(),
        "btn_grade_setback": i18n.btn.setback(),
        "btn_grade_clear": i18n.btn.clear(),
        "btn_grade_cancel": i18n.btn.cancel(),
        "radio_grade": grades,
    }
