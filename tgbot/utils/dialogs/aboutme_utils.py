from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from tgbot.db import Repo
from tgbot.db.dao import UserDAO, StatusDAO
from .text_utils import *

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# О себе
async def create_aboutme_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name: str = await create_name_text(dialog_manager, i18n)
    age: str = await create_age_text(dialog_manager, i18n)
    gender: str = await create_gender_text(dialog_manager, i18n)

    log_dev.debug(" create_aboutme_text: gender: %s", gender)

    if age and name:
        age = lower_string(age)
    if gender and (name or age):
        gender = 'и ' + lower_string(gender)

    str_list = [s for s in [name, age, gender] if s]

    return ', '.join(str_list) if str_list else i18n.txt.aboutme.menothing()


# Имя
async def create_name_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    name: str = await get_item_value(item_id='name', host='user', dialog_manager=dialog_manager)
    return ' '.join([i18n.txt.name.before.short(), name]) if name else ''


async def get_name_string(dialog_manager: DialogManager) -> str:
    name: str = await get_item_value(item_id='name', host='user', dialog_manager=dialog_manager)
    return create_name_string(name)


async def show_name_string(dialog_manager: DialogManager) -> str:
    name: str = await get_item_value(item_id='name', host='user', dialog_manager=dialog_manager)
    return create_show_name_string(name)


# Возраст
async def create_age_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    age: int = await get_item_value(item_id='age', host='user', dialog_manager=dialog_manager)
    age_f_str: str = create_age_f_string(age, i18n)

    return ' '.join([i18n.txt.age.before.short(), age_f_str]) if age else ''


async def create_age_f_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    age: int = await get_item_value(item_id='age', host='user', dialog_manager=dialog_manager)
    age_f_str: str = create_age_f_string(age, i18n)

    return age_f_str if age else ''


async def get_age_string(dialog_manager: DialogManager) -> str:
    age: int = await get_item_value(item_id='age', host='user', dialog_manager=dialog_manager)
    return create_age_string(age)


# Пол
async def create_gender_text(dialog_manager: DialogManager, i18n: TranslatorRunner) -> str:
    gender_item: str = await get_item_value(item_id='gender', host='user', dialog_manager=dialog_manager)
    gender: Gender = Gender(gender_item) if gender_item else None
    gender_str: str = create_gender_string(gender, i18n)

    return ' '.join([i18n.txt.gender.before.short() + ' -', gender_str]) if gender_str else ''


async def get_gender_string(dialog_manager: DialogManager) -> str | None:
    """
    Получить значение виджета 'Пол' как строку

    :param dialog_manager:
    :return:
    """
    return await get_item_value(item_id='gender', host='user', dialog_manager=dialog_manager)


# Состояние
async def create_status_text(dialog_manager: DialogManager) -> str:
    status: str = await get_item_value(item_id='status_text', host='status', dialog_manager=dialog_manager)
    return create_status_string(status)


async def get_status_string(dialog_manager: DialogManager) -> str:
    status: str = await get_item_value(item_id='status_text', host='status', dialog_manager=dialog_manager)
    return status if status else ''


# Оценка состояния
async def create_grade_text(dialog_manager: DialogManager, grades: dict) -> str:
    grade_item: str | int = await get_item_value(item_id='grade', host='status', dialog_manager=dialog_manager)
    grade_str: str = create_grade_string(grade_item)
    grade_f_str: str = create_grade_f_string(grade_item)

    log_dev.debug(" create_grade_text: grade_f_str: %s", grade_f_str)
    return '   '.join([grade_f_str, grades[grade_str]]) if grade_item else ''


async def get_grade_str(dialog_manager: DialogManager) -> str | None:
    """
    Получить значение виджета 'Оценка состояния' как число

    :param dialog_manager: 
    :return: 
    """
    return await get_item_value(item_id='grade', host='status', dialog_manager=dialog_manager)


# Виджеты ====================================================================================================

async def get_item_value(item_id: str, host: str, dialog_manager: DialogManager) -> int | str | None:
    """
    Получить значение любого виджета, или None, если виджета нет, или его значение None

    :param item_id:
    :param host:
    :param dialog_manager:
    :return:
    """
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
async def update_user(dialog_manager: DialogManager) -> None:
    widget_data = dialog_manager.current_context().widget_data

    state: FSMContext = dialog_manager.middleware_data['state']
    state_data: dict = await state.get_data()
    user: UserDAO = state_data.get('user')

    if 'name' in widget_data:
        user_name = widget_data['name']
        user.name = user_name

        # Обновление имени пользователя в общем контексте state data
        await state.update_data({'user_data': {'user_name': user_name}})
    if 'age' in widget_data:
        user.age = widget_data['age']
    if 'gender' in widget_data:
        user.gender = create_grade_string(widget_data['gender'])

    repo: Repo = dialog_manager.middleware_data.get('repo')
    await repo.user.update(user)


# Сохранить состояние
async def add_status(dialog_manager: DialogManager) -> None:
    widget_data = dialog_manager.current_context().widget_data

    state_data: dict = await dialog_manager.middleware_data['state'].get_data()
    status: StatusDAO = state_data.get('status')

    if 'status_text' in widget_data:
        status.status_text = widget_data['status_text']
    if 'grade' in widget_data:
        status.grade = int(widget_data['grade'])
    status.id = None

    repo: Repo = dialog_manager.middleware_data.get('repo')
    await repo.status.add(status)
