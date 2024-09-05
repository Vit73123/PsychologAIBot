from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Radio
from fluentogram import TranslatorRunner

from tgbot.db import Repo
from tgbot.db.dao import StatusDAO, UserDAO
from tgbot.db.models.user import Gender
from tgbot.dialogs.states import Aboutme
from tgbot.tools.logger import get_logger_dev
from tgbot.utils import (create_gender_string,
                         create_after_years_string)

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
    log_dev.debug(" About me: get_aboutme: context: %s", dialog_manager.current_context())

    await state.set_state(Aboutme.start)
    state_data = await state.get_data()
    log_dev.debug(" About me: get_aboutme: FSM: state: %s, context: %s", await state.get_state(), state_data)

    if 'user' not in state_data:
        user: UserDAO = await repo.user.get(dialog_manager.start_data['user_id'])
        await state.update_data({'user': user})
        dialog_manager.dialog_data.update({'updated_items': set()})

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

    state_data = await state.get_data()
    log_dev.debug(" About me: get_aboutme: FSM: state: %s, context: %s", await state.get_state(), state_data)

    user: UserDAO = state_data['user']
    if 'status' not in state_data:
        status: StatusDAO = await repo.status.get_last_by_user_id(dialog_manager.start_data['user_id'])
        status_data = {'status': status}
        state_data.update(status_data)
        await state.update_data(status_data)
    status = state_data['status']

    aboutme_txt = _create_aboutme_text(user=user, dialog_manager=dialog_manager, i18n=i18n)
    status_txt = _create_status_text(status=status, dialog_manager=dialog_manager)
    grade_txt = _create_grade_text(status=status, dialog_manager=dialog_manager, grades=grades)

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
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Name: get_name: context: %s", dialog_manager.current_context())

    return {
        "win_name": i18n.win.aboutme.profile.name(),
        "btn_name_setback": i18n.btn.setback(),
        "btn_name_clear": i18n.btn.clear(),
        "btn_name_cancel": i18n.btn.cancel.getback(),
    }


# Возраст
async def get_age(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_age": i18n.win.aboutme.profile.age(),
        "btn_age_setback": i18n.btn.setback(),
        "btn_age_clear": i18n.btn.clear(),
        "btn_age_cancel": i18n.btn.cancel.getback(),
    }


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
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    return {
        "win_status": i18n.win.aboutme.profile.status(),
        "btn_status_setback": i18n.btn.setback(),
        "btn_status_clear": i18n.btn.clear(),
        "btn_status_cancel": i18n.btn.cancel(),
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
        "btn_grade_setback": i18n.btn.setback(),
        "btn_grade_clear": i18n.btn.clear(),
        "btn_grade_cancel": i18n.btn.cancel(),
        "radio_grade": grades,
    }


# Profile =====================================================================================================

def _create_aboutme_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner,
                         new_line: bool = True) -> str:
    updated_items: set = dialog_manager.dialog_data.get('updated_items')

    inp_name: TextInput = dialog_manager.find('inp_name') if 'name' in updated_items else None
    inp_age: TextInput = dialog_manager.find('inp_age') if 'age' in updated_items else None
    radio_gender: Radio = dialog_manager.find('radio_gender') if 'gender' in updated_items else None

    name_value: str = inp_name.get_value() if inp_name else user.name
    name_value = name_value if name_value else dialog_manager.start_data.get('user_name')

    age_value: int = inp_age.get_value() if inp_age else user.age
    gender_checked: Gender = radio_gender.get_checked() if radio_gender else None
    gender_value = gender_checked if gender_checked != 0 else None

    name: str = ' '.join([i18n.txt.name.before(), '<b>' + name_value + '</b>']) if name_value else ''
    age: str = ' '.join(
        [i18n.txt.age.before(), '<b>' + str(age_value) + '</b>',
         create_after_years_string(years=age_value, i18n=i18n)]) if age_value else ''
    gender: str = ' '.join(
        [i18n.txt.gender.before() + ' -',
         '<b>' + create_gender_string(gender=gender_value, i18n=i18n) + '</b>']) if gender_value else ''

    if new_line:
        name = (name[0].upper() + name[1:]) if name else name

    if age and not name:
        age = age[0].upper() + age[1:]
    if gender:
        if not (name and age):
            gender = gender[0].upper() + gender[1:]
        else:
            gender = ', и ' + gender

    str_list = [s for s in [name, age, gender] if s]

    return ', '.join(str_list)


# Status ======================================================================================================

def _create_status_text(status: StatusDAO, dialog_manager: DialogManager) -> str | None:
    if status:
        updated_items: set = dialog_manager.dialog_data.get('updated_items')
        inp_status: TextInput = dialog_manager.find('inp_status') if 'inp_status' in updated_items else None
        return inp_status.get_value() if inp_status else status.text
    else:
        return None


def _create_grade_text(status: StatusDAO, dialog_manager: DialogManager, grades: dict) -> str | None:
    if status:
        updated_items: set = dialog_manager.dialog_data.get('updated_items')
        radio_grade: Radio = dialog_manager.dialog_data.get('radio_grade') if 'radio_grade' in updated_items else None
        grade_checked: int = radio_grade.get_checked()
        grade: int = grade_checked if grade_checked else status.grade
        return f"{grade:+} {grades[str(grade)]}"
    else:
        return None


# Reset data ==================================================================================================

def _reset_all(dialog_manager: DialogManager):
    dialog_manager.dialog_data.clear()
    dialog_manager.current_context().widget_data.clear()
