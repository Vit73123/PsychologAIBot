from logging import getLogger

from aiogram_dialog import DialogManager

from tgbot.tools.logger import get_logger_dev
from .text_utils import *
from ...db import Repo
from ...db.dao import UserDAO, StatusDAO

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# О себе
async def create_aboutme_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name: str = await create_name_text(dialog_manager, i18n)
    age: str = await create_age_text(dialog_manager, i18n)
    gender: str = await create_gender_text(dialog_manager, i18n)

    if age and name:
        age = lower_text(age)
    if gender and (name or age):
        gender = 'и ' + lower_text(gender)

    str_list = [s for s in [name, age, gender] if s]

    return ', '.join(str_list) if str_list else i18n.txt.aboutme.menothing()


# Имя
async def create_name_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name: str = await get_item_value(item_id='name', host='user', dialog_manager=dialog_manager)
    return ' '.join([i18n.txt.name.before.short(), '<b>' + name + '</b>']) if name else ''


async def get_name_string(dialog_manager: DialogManager) -> str:
    name: str = await get_item_value(item_id='name', host='user', dialog_manager=dialog_manager)
    return create_name_string(name)


# Возраст
async def create_age_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    age: int = await get_item_value(item_id='age', host='user', dialog_manager=dialog_manager)
    age_f_str: str = create_age_f_string(age, i18n)

    return ' '.join([i18n.txt.age.before.short(), '<b>' + age_f_str + '</b>']) if age else ''


async def get_age_string(dialog_manager: DialogManager) -> str:
    age: int = await get_item_value(item_id='age', host='user', dialog_manager=dialog_manager)
    return create_age_string(age)


# Пол
async def create_gender_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    gender: Gender = await get_item_value(item_id='gender', host='user', dialog_manager=dialog_manager)
    gender_f_str: str = create_gender_f_string(gender, i18n)

    return ' '.join([i18n.txt.gender.before.short() + ' -', '<b>' + gender_f_str + '</b>']) if gender_f_str else ''


async def get_gender_string(dialog_manager: DialogManager) -> str:
    gender: Gender = await get_item_value(item_id='gender', host='user', dialog_manager=dialog_manager)
    return create_gender_string(gender)


# Состояние
async def create_status_text(dialog_manager: DialogManager) -> str:
    status: str = await get_item_value(item_id='status_text', host='status', dialog_manager=dialog_manager)
    return create_status_string(status)


async def get_status_string(dialog_manager: DialogManager) -> str:
    status: str = await get_item_value(item_id='status_text', host='status', dialog_manager=dialog_manager)
    return status if status else ''


# Оценка состояния
async def create_grade_text(dialog_manager: DialogManager, grades: dict) -> str:
    grade: int = await get_item_value(item_id='grade', host='status', dialog_manager=dialog_manager)
    grade_str: str = create_grade_string(grade)
    grade_f_str = create_grade_f_string(grade)

    return '   '.join([grade_f_str, grades[grade_str]]) if grade else ''


async def get_grade_string(dialog_manager: DialogManager) -> str:
    grade: int = await get_item_value(item_id='grade', host='status', dialog_manager=dialog_manager)
    return create_grade_string(grade) if grade else ''


# Виджеты ====================================================================================================

# Получить значение любого виджета, или None, если виджета нет, или его значение None
async def get_item_value(item_id: str, host: str, dialog_manager: DialogManager) -> Gender | int | str | None:
    log_dev.debug(" get_item_value: item_id: %s", item_id)
    widget_data: dict = dialog_manager.current_context().widget_data
    if item_id in widget_data:
        return widget_data[item_id]
    else:
        state_data: dict = await dialog_manager.middleware_data['state'].get_data()
        obj = state_data.get(host)
        return getattr(obj, item_id)


# Окна обработки Виджетов =====================================================================================

# Кнопки Reset, Cancel
def item_reset(item_id: str, dialog_manager: DialogManager) -> None:
    widget_data: dict = dialog_manager.current_context().widget_data
    if item_id in widget_data:
        widget_data.pop(item_id)


# Кнопка Clear
def item_clear(item_id: str, dialog_manager: DialogManager) -> None:
    dialog_manager.current_context().widget_data.update({item_id: None})


# Установить значение виджета
def item_set(value: str | int | None, item_id: str, dialog_manager) -> None:
    dialog_manager.current_context().widget_data[item_id] = value


# Профиль =====================================================================================================

# Кнопка Reset
def profile_reset(dialog_manager: DialogManager) -> None:
    dialog_manager.current_context().widget_data.clear()


# Кнопка Clear
def profile_clear(dialog_manager: DialogManager) -> None:
    dialog_manager.current_context().widget_data.update({
        'name': None,
        'age': None,
        'gender': None,
        'status_text': None,
        'grade': None,
    })


# Сохранить пользователя
async def save_user(dialog_manager: DialogManager) -> None:
    widget_data = dialog_manager.current_context().widget_data

    name: str = widget_data['name'] if 'name' in widget_data else None
    age: int = widget_data['age'] if 'age' in widget_data else None
    gender: str = create_grade_string(widget_data['gender']) if 'gender' in widget_data else None

    state_data: dict = await dialog_manager.middleware_data['state'].get_data()
    user: UserDAO = state_data.get('user')

    if name:
        user.name = name
    if age:
        user.age = age
    if gender:
        user.gender = gender

    repo: Repo = dialog_manager.middleware_data.get('repo')
    await repo.user.update(user)


# Сохранить состояние
async def save_status(dialog_manager: DialogManager) -> None:
    widget_data = dialog_manager.current_context().widget_data

    status_text: str = widget_data['status_text'] if 'status_text' in widget_data else None
    grade: int = int(create_grade_string(widget_data['grade'])) if 'grade' in widget_data else None

    state_data: dict = await dialog_manager.middleware_data['state'].get_data()
    status: StatusDAO = state_data.get('status')

    if status_text:
        status.status_text = status_text
    if grade:
        status.grade = grade

    repo: Repo = dialog_manager.middleware_data.get('repo')
    await repo.status.update(status)
