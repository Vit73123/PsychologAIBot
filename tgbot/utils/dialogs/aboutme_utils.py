from logging import getLogger

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Radio

from tgbot.db.dao import UserDAO, StatusDAO
from tgbot.tools.logger import get_logger_dev
from .text_utils import *

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# Aboutme
def create_aboutme_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name: str = create_name_text(user, dialog_manager, i18n)
    age: str = create_age_text(user, dialog_manager, i18n)
    gender: str = create_gender_text(user, dialog_manager, i18n)

    if age and name:
        age = lower_text(age)
    if gender and (name or age):
        gender = 'и ' + lower_text(gender)

    str_list = [s for s in [name, age, gender] if s]

    return ', '.join(str_list) if str_list else i18n.txt.aboutme.menothing()


# Name
def create_name_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name: str = get_name_string(user, dialog_manager)
    return ' '.join([i18n.txt.name.before.short(), '<b>' + name + '</b>']) if name else ''


def get_name_string(user: UserDAO, dialog_manager: DialogManager) -> str:
    name: str = get_item_value('name', user, dialog_manager)
    return create_name_string(name)


# Age
def create_age_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    age: int = get_item_value('age', user, dialog_manager)
    age_f_str: str = create_age_f_string(age, i18n)

    return ' '.join([i18n.txt.age.before.short(), '<b>' + age_f_str + '</b>']) if age else ''


def get_age_string(user: UserDAO, dialog_manager: DialogManager) -> str:
    age: int = get_item_value('age', user, dialog_manager)
    return create_age_string(age)


# Gender
def create_gender_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    gender: Gender = get_item_checked('gender', user, dialog_manager)
    gender_f_str: str = create_gender_f_string(gender, i18n)

    return ' '.join([i18n.txt.gender.before.short() + ' -', '<b>' + gender_f_str + '</b>']) if gender_f_str else ''


def get_gender_string(user: UserDAO, dialog_manager: DialogManager) -> str:
    gender: Gender = get_item_checked('gender', user, dialog_manager)
    return create_gender_string(gender)


# Status
def create_status_text(status: StatusDAO, dialog_manager: DialogManager) -> str:
    status: str = get_status_string(status, dialog_manager)
    return create_status_string(status)


def get_status_string(status: StatusDAO, dialog_manager: DialogManager) -> str:
    status: str = get_item_value('status_text', status, dialog_manager)
    return status if status else ''


# Grade
def create_grade_text(status: StatusDAO, dialog_manager: DialogManager, grades: dict) -> str:
    grade: int = get_item_checked('grade', status, dialog_manager)
    grade_str: str = create_grade_string(grade)
    grade_f_str = create_grade_f_string(grade)

    return '   '.join([grade_f_str, grades[grade_str]]) if grade else ''


def get_grade_string(status: StatusDAO, dialog_manager: DialogManager) -> str:
    grade: int = get_item_checked('grade', status, dialog_manager)
    return create_grade_string(grade) if grade else ''


# Get item value
def get_item_value(item_id: str, obj: UserDAO | StatusDAO, dialog_manager: DialogManager) -> Gender | int | str | None:
    log_dev.debug(" get_item_value: item_id: %s", item_id)
    if item_id in dialog_manager.dialog_data.get('updated_items'):
        item: TextInput | Radio = dialog_manager.find(item_id)
        log_dev.debug(" get_item_value: item.get_value(): %s", item.get_value())
        return item.get_value()
    else:
        log_dev.debug(" get_item_value: getattr(obj, item_id): %s", getattr(obj, item_id))
        return getattr(obj, item_id)


# Get item value
def get_item_checked(item_id: str, obj: UserDAO | StatusDAO,
                     dialog_manager: DialogManager) -> Gender | int | str | None:
    log_dev.debug(" get_item_checked: item_id: %s", item_id)
    if item_id in dialog_manager.dialog_data.get('updated_items'):
        item: Radio = dialog_manager.find(item_id)
        log_dev.debug(" get_item_checked: item.get_checked(): %s", item.get_checked())
        return item.get_checked()
    else:
        log_dev.debug(" get_item_checked: getattr(obj, item_id): %s", getattr(obj, item_id))
        return getattr(obj, item_id)


# Set profile empty
def set_profile_empty(dialog_manager: DialogManager, ) -> None:
    dialog_manager.current_context().widget_data.clear()
    dialog_manager.dialog_data.update({
        'updated_items': {
            'name', 'age', 'gender', 'status_text', 'grade'}
    })
