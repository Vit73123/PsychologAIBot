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

# Set profile empty

def set_profile_empty(dialog_manager: DialogManager, ) -> None:
    dialog_manager.current_context().widget_data.clear()
    dialog_manager.dialog_data.update({
        'updated_items': {
            'inp_name', 'inp_age', 'radio_gender', 'inp_status', 'radio_grade'}
    })


# Aboutme text

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
    name_str: str = _create_name_string(user, dialog_manager)
    return ' '.join([i18n.txt.name.before.short(), '<b>' + name_str + '</b>']) if name_str else ''


def _create_name_string(user: UserDAO, dialog_manager: DialogManager) -> str:
    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    inp_name: TextInput = dialog_manager.find('inp_name')
    name_str: str = inp_name.get_value() if 'name' in updated_items else user.name

    return name_str.strip() if name_str else ''


def _create_age_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    age_num: int = _create_age_num(user, dialog_manager)

    return ' '.join(
        [i18n.txt.age.before.short(), '<b>' + str(age_num) + '</b>',
         create_after_years_string(years=age_num, i18n=i18n)]) if age_num else ''


def _create_age_num(user: UserDAO, dialog_manager: DialogManager) -> int:
    updated_items: set = dialog_manager.dialog_data.get('updated_items')
    inp_age: TextInput = dialog_manager.find('inp_age')

    age_num: int = inp_age.get_value() if 'age' in updated_items else user.age

    return age_num


def _create_gender_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    gender_str: str = _create_gender_string(user, dialog_manager, i18n)

    return ' '.join(
        [i18n.txt.gender.before.short() + ' -',
         '<b>' + gender_str + '</b>']) if gender_str else ''


def get_gender_string(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> int | None:
    gender_str: str = None
    if 'gender' in dialog_manager.dialog_data.get('updated_items'):
        radio_gender: Radio = dialog_manager.find('radio_gender')
        gender_checked: Gender = radio_gender.get_checked()
    else:
        gender_checked: Gender = radio_gender.get_checked()
    gender_enum = gender_checked if gender_checked != 0 else None

    return get_gender_string(gender=gender_enum, i18n=i18n)


def get_gender(dialog_manager: DialogManager, i18n: TranslatorRunner) -> Gender | None:
    if 'gender' in dialog_manager.dialog_data.get('updated_items'):
        radio_gender: Radio = dialog_manager.find('radio_gender')
        return radio_gender.get_checked()
    else:
        return None


# Status

def create_status_text(status: StatusDAO, dialog_manager: DialogManager) -> str | None:
    status_text = None
    if status:
        updated_items: set = dialog_manager.dialog_data.get('updated_items')
        if 'status' in updated_items:
            inp_status: TextInput = dialog_manager.find('inp_status')
            status_text = inp_status.get_value()
        else:
            status_text = status.text

    log_dev.debug(" create_status_text: %s", status_text)
    return status_text if status_text is not None else ''


# Grade

def create_grade_text(status: StatusDAO, dialog_manager: DialogManager, grades: dict) -> str:
    grade_num = get_grade_num(status, dialog_manager)
    return f"{grade_num:+} {grades[str(grade_num)]}" if grade_num else ''


def get_grade_num(status: StatusDAO, dialog_manager: DialogManager) -> int | None:
    grade_num: int = None
    if status:
        updated_items: set = dialog_manager.dialog_data.get('updated_items')
        if 'grade' in updated_items:
            radio_grade: Radio = dialog_manager.find('radio_grade')
            grade_num = radio_grade.get_checked()
        else:
            grade_num = status.grade

    log_dev.debug(" create_grade_num: %d", grade_num)
    return grade_num


def get_item_value(item_id: str, entity: UserDAO | StatusDAO, dialog_manager: DialogManager) -> Gender | int | str | None:
    if item_id in dialog_manager.dialog_data.get('updated_items'):
        item: TextInput | Radio = dialog_manager.find(item_id)
        return item.get_value()
    else:
        return entity


