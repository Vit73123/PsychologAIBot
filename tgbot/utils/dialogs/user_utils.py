from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Radio
from fluentogram import TranslatorRunner

from tgbot.db.dao import UserDAO, StatusDAO
from tgbot.db.models.user import Gender
from tgbot.utils import create_user_name_text, create_after_years_string, get_gender_string


# Aboutme

def create_aboutme_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner,
                        new_line: bool = True) -> str:
    name: str = create_name_text(user, dialog_manager, i18n)
    age: str = _create_age_text(user, dialog_manager, i18n)
    gender: str = _create_gender_text(user, dialog_manager, i18n)

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


def create_name_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name_str: str = _create_name_string(user, dialog_manager, i18n)
    return ' '.join([i18n.txt.name.before(), '<b>' + name_str + '</b>']) if name_str else ''


def _create_name_string(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    inp_name: TextInput = dialog_manager.find('inp_name')

    name_str: str = inp_name.get_value() if 'name' in updated_items else user.name
    name_str = name_str if name_str else create_user_name_text(name_str, i18n)

    return name_str


def _create_age_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    age_num: int = _create_age_num(user, dialog_manager, i18n)

    return ' '.join(
        [i18n.txt.age.before(), '<b>' + str(age_num) + '</b>',
         create_after_years_string(years=age_num, i18n=i18n)]) if age_num else ''


def _create_age_num(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> int:
    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    inp_age: TextInput = dialog_manager.find('inp_age')

    age_num: int = inp_age.get_value() if 'age' in updated_items else user.age

    return age_num


def _create_gender_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    gender_str: str = _create_gender_string(user, dialog_manager, i18n)

    return ' '.join(
        [i18n.txt.gender.before() + ' -',
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


def create_grade_text(status: StatusDAO, dialog_manager: DialogManager, grades: dict) -> str | None:
    if status:
        updated_items: set = dialog_manager.dialog_data.get('updated_items')
        radio_grade: Radio = dialog_manager.dialog_data.get('radio_grade') if 'radio_grade' in updated_items else None
        grade_checked: int = radio_grade.get_checked() if radio_grade else None
        grade: int = grade_checked if grade_checked else status.grade
        return f"{grade:+} {grades[str(grade)]}"
    else:
        return None
