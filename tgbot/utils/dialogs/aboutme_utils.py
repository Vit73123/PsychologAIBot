from logging import getLogger

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Radio
from fluentogram import TranslatorRunner

from tgbot.db.dao import UserDAO, StatusDAO
from tgbot.db.models.user import Gender
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.common import create_after_years_string, get_gender_string, lower_text

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# Aboutme

def create_aboutme_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner,
                        new_line: bool = True) -> str:
    name: str = create_name_text(user, dialog_manager, i18n)
    age: str = _create_age_text(user, dialog_manager, i18n)
    gender: str = _create_gender_text(user, dialog_manager, i18n)

    if new_line:
        name = (name[0].upper() + name[1:]) if name else name

    if age and name:
        age = lower_text(age)
    if gender and (name or age):
        gender = 'и ' + lower_text(gender)

    str_list = [s for s in [name, age, gender] if s]

    return ', '.join(str_list) if str_list else i18n.txt.aboutme.menothing()


def create_name_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name_str: str = _create_name_string(user, dialog_manager, i18n)
    return ' '.join([i18n.txt.name.before.short(), '<b>' + name_str + '</b>']) if name_str else ''


def _create_name_string(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    inp_name: TextInput = dialog_manager.find('inp_name')
    name_str: str = inp_name.get_value() if 'name' in updated_items else user.name

    return name_str.strip() if name_str else ''


def _create_age_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    age_num: int = _create_age_num(user, dialog_manager, i18n)

    return ' '.join(
        [i18n.txt.age.before.short(), '<b>' + str(age_num) + '</b>',
         create_after_years_string(years=age_num, i18n=i18n)]) if age_num else ''


def _create_age_num(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> int:
    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    inp_age: TextInput = dialog_manager.find('inp_age')

    age_num: int = inp_age.get_value() if 'age' in updated_items else user.age

    return age_num


def _create_gender_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    gender_str: str = _create_gender_string(user, dialog_manager, i18n)

    return ' '.join(
        [i18n.txt.gender.before.short() + ' -',
         '<b>' + gender_str + '</b>']) if gender_str else ''


def _create_gender_string(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    updated_items: set = dialog_manager.dialog_data.get('updated_items')

    radio_gender: Radio = dialog_manager.find('radio_gender')

    gender_checked: Gender = radio_gender.get_checked() if 'gender' in updated_items else user.gender
    gender_enum = gender_checked if gender_checked != 0 else None

    return get_gender_string(gender=gender_enum, i18n=i18n)


# Status

def create_status_text(status: StatusDAO, dialog_manager: DialogManager) -> str | None:
    if status:
        updated_items: set = dialog_manager.dialog_data.get('updated_items')
        inp_status: TextInput = dialog_manager.find('inp_status') if 'inp_status' in updated_items else None
        return inp_status.get_value() if inp_status else status.text
    else:
        return None


# Grade

def create_grade_text(status: StatusDAO, dialog_manager: DialogManager, grades: dict) -> str | None:
    if status:
        updated_items: set = dialog_manager.dialog_data.get('updated_items')
        radio_grade: Radio = dialog_manager.dialog_data.get('radio_grade') if 'radio_grade' in updated_items else None
        grade_checked: int = radio_grade.get_checked() if radio_grade else None
        grade: int = grade_checked if grade_checked else status.grade
        return f"{grade:+} {grades[str(grade)]}"
    else:
        return None
