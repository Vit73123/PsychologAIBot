from logging import getLogger

from aiogram_dialog import DialogManager

from tgbot.db.dao import UserDAO, StatusDAO
from tgbot.tools.logger import get_logger_dev
from .text_utils import *

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# О себе
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


# Имя
def create_name_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name: str = get_name_string(user, dialog_manager)
    return ' '.join([i18n.txt.name.before.short(), '<b>' + name + '</b>']) if name else ''


def get_name_string(user: UserDAO, dialog_manager: DialogManager) -> str:
    name: str = get_item_value('name', user, dialog_manager)
    return create_name_string(name)


# Возраст
def create_age_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    age: int = get_item_value('age', user, dialog_manager)
    age_f_str: str = create_age_f_string(age, i18n)

    return ' '.join([i18n.txt.age.before.short(), '<b>' + age_f_str + '</b>']) if age else ''


def get_age_string(user: UserDAO, dialog_manager: DialogManager) -> str:
    age: int = get_item_value('age', user, dialog_manager)
    return create_age_string(age)


# Gender
def create_gender_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    gender: Gender = get_item_value('gender', user, dialog_manager)
    gender_f_str: str = create_gender_f_string(gender, i18n)

    return ' '.join([i18n.txt.gender.before.short() + ' -', '<b>' + gender_f_str + '</b>']) if gender_f_str else ''


def get_gender_string(user: UserDAO, dialog_manager: DialogManager) -> str:
    gender: Gender = get_item_value('gender', user, dialog_manager)
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
    grade: int = get_item_value('grade', status, dialog_manager)
    grade_str: str = create_grade_string(grade)
    grade_f_str = create_grade_f_string(grade)

    return '   '.join([grade_f_str, grades[grade_str]]) if grade else ''


def get_grade_string(status: StatusDAO, dialog_manager: DialogManager) -> str:
    grade: int = get_item_value('grade', status, dialog_manager)
    return create_grade_string(grade) if grade else ''


# Get item value
def get_item_value(item_id: str, obj: UserDAO | StatusDAO, dialog_manager: DialogManager) -> Gender | int | str | None:
    log_dev.debug(" get_item_value: item_id: %s", item_id)
    value = None
    if item_id in dialog_manager.dialog_data.get('updated'):
        widget_data = dialog_manager.current_context().widget_data
        if item_id in widget_data:
            value = widget_data[item_id]
    else:
        value = getattr(obj, item_id)
    return value


# Виджеты =====================================================================================================

# Восстановить временное состояние виджета до начального: значение, состояние в updated
def item_reset_to_state(item_id: str, dialog_manager) -> None:
    dialog_manager.dialog_data['item_state']['new_updated'] = dialog_manager.dialog_data['item_state']['old_updated']
    dialog_manager.dialog_data['item_state']['new_updated'] = dialog_manager.dialog_data['item_state']['old_updated']


# -------------------------------------------------------------------------------------------------------------

# Виджет во временном состоянии: в окне виджета со снимком состояния item_state в dialog_data

# Кнопки reset, clear окна обработки виджета

def item_reset(item_id: str, dialog_manager: DialogManager) -> None:
    item_reset_value(item_id=item_id, dialog_manager=dialog_manager)
    item_reset_updated(item_id=item_id, dialog_manager=dialog_manager)


def item_reset_value(item_id: str, dialog_manager: DialogManager) -> None:
    log_dev.debug(" item_reset_value: item_id: %s", item_id)

    dialog_manager.current_context().widget_data[item_id] = dialog_manager.dialog_data['item_state']['old_value']


def item_reset_updated(item_id: str, dialog_manager: DialogManager) -> None:
    log_dev.debug(" item_reset_updated: item_id: %s", item_id)

    dialog_manager.dialog_data['item_state']['new_updated'] = dialog_manager.dialog_data['item_state']['old_updated']


# -------------------------------------------------------------------------------------------------------------

# Кнопки ok, cancel окна обработки виджета

# Задать "пустое" состояние виджета: значение, добавить в updated
def item_clear(item_id: str, dialog_manager) -> None:
    item_set_value(value=None, item_id=item_id, dialog_manager=dialog_manager)
    item_add_to_updated(item_id, dialog_manager)


# Установить только значение виджета: необходимо в cancel_click окна обработки виджета
def item_set_value(value: str | int | None, item_id: str, dialog_manager) -> None:
    dialog_manager.current_context().widget_data[item_id] = value
    item_add_to_updated(item_id='name', dialog_manager=dialog_manager)


# Обновить updated в соответствии с состоянием виджета: необходимо в ok_click окна обработки виджета
def item_set_updated(item_id: str, dialog_manager: DialogManager):
    item_state = dialog_manager.dialog_data['item_state']
    if item_state['updated']:
        item_add_to_updated(item_id)
    else:
        item_remove_from_updated(item_id)


# -------------------------------------------------------------------------------------------------------------

# Восстановить профиль: задать значения "пустые" состояния для всех виджетов профиля: значения, состояния в updated
# Значения при отображении не "подтягиваются" из базы данных, а фактически остаются "пустыми"
def profile_clear(dialog_manager: DialogManager, ) -> None:
    dialog_manager.current_context().widget_data.clear()
    dialog_manager.dialog_data.update({
        'updated': {
            'name', 'age', 'gender', 'status_text', 'grade'}
    })


# "Очистить" значения всех виджетов.
# В таком состоянии
# - виджеты в состоянии "изменённый" (присутствуют в set updated)
# при выводе "занимают место" начальных значений из базы данных.
# - виджеты состояния "неизменённый" (отсутствуют в set updated),
# при выводе "освобождают место" начальных значений из базы данных, включая новые значения None.
def profile_clear_values(dialog_manager: DialogManager, ) -> None:
    dialog_manager.current_context().widget_data.clear()


# Сделать все ВИДЖЕТЫ "ИЗМЕНЁННЫМИ". Виджеты "занимают место" начальных значений из базы данных,
# независимо от того, есть ли у виджета значение.
# Значения виджетов Null будут отображаться пустыми строками "поверх" значений базы данных
def profile_set_updated(dialog_manager: DialogManager, ) -> None:
    dialog_manager.dialog_data.update({
        'updated': {
            'name', 'age', 'gender', 'status_text', 'grade'}
    })


# Сделать все ВИДЖЕТЫ "НЕИЗМЕНЁННЫМИ". Виджеты "освобождают место" для начальных значений из базы данных.
# независимо от того, есть ли у виджета значение.
# Значения базы данных Null будут отображаться пустыми строками "поверх" значений виджетов
def profile_clear_updated(dialog_manager: DialogManager, ) -> None:
    dialog_manager.dialog_data.update({
        'updated': set()
    })


# -------------------------------------------------------------------------------------------------------------

# Добавить виджет в updated
def item_add_to_updated(item_id: str, dialog_manager: DialogManager):
    updated: set = dialog_manager.dialog_data.get('updated')
    updated.add(item_id)
    dialog_manager.dialog_data.update({'updated': updated})


# Удалить виджет из updated
def item_remove_from_updated(item_id: str, dialog_manager: DialogManager):
    updated: set = dialog_manager.dialog_data.get('updated')
    updated.discard(item_id)
    dialog_manager.dialog_data.update({'updated': updated})
