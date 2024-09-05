from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.db.dao import UserDAO
from tgbot.db.models import User
from tgbot.db.models.user import Gender
from tgbot.errors.errors import *
from tgbot.tools.jinja import escape_text
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def create_user_from_bot(bot_user) -> User:
    return User(
        user_id=bot_user.id,
        username=bot_user.username,
        first_name=bot_user.first_name,
        last_name=bot_user.last_name,
    )


def create_user_to_dao(user: User) -> UserDAO | None:
    if user:
        return UserDAO(
            user_id=user.id,
            name=user.name,
            gender=user.gender,
            age=user.age
        )


def create_user_from_dao(user_dao: UserDAO) -> User | None:
    if user_dao:
        user = User()
        user.id = user_dao.id
        user.name = user_dao.name
        user.gender = user_dao.gender
        user.age = user_dao.age
        return user


def create_user_name_text(name: str, i18n: TranslatorRunner) -> str:
    return escape_text(
        i18n.txt.name.anonim() if not name else name
    )


# def create_user_aboutme_text(user: UserDAO, dialog_manager: DialogManager, i18n: TranslatorRunner,
#                              new_line: bool = True) -> str:
#     name_widget:  = dialog_manager.find('inp_name')
#     age_widget = dialog_manager.find('inp_age')
#     gender_widget = dialog_manager.find('radio_gender')
#
#     name_: str = user.name if not name_widget else name_widget
#     age_: int = user.age if 'age' not in widgets_data else widgets_data['age']
#     gender_: Gender = user.gender if 'gender' not in widgets_data else widgets_data['gender']
#
#     name = ' '.join([i18n.txt.name.before(), '<b>' + name_ + '</b>']) if name_ else ''
#     age: str = ' '.join(
#         [i18n.txt.age.before(), '<b>' + str(age_) + '</b>', _after_years_string(years=age_, i18n=i18n)]) if age_ else ''
#     gender: str = ' '.join(
#         ['и ' + i18n.txt.gender.before() + ' -',
#          '<b>' + create_gender_string(gender=gender_, i18n=i18n) + '</b>']) if gender_ else ''


# def create_user_aboutme_text(user: UserDAO, user_upd: dict, i18n: TranslatorRunner, new_line: bool = True) -> str:
#     name_: str = user.name if 'name' not in user_upd else user_upd['name']
#     age_: int = user.age if 'age' not in user_upd else user_upd['age']
#     gender_: Gender = user.gender if 'gender' not in user_upd else user_upd['gender']
#
#     name = ' '.join([i18n.txt.name.before(), '<b>' + name_ + '</b>']) if name_ else ''
#     age: str = ' '.join(
#         [i18n.txt.age.before(), '<b>' + str(age_) + '</b>', create_after_years_string(years=age_, i18n=i18n)]) if age_ else ''
#     gender: str = ' '.join(
#         ['и ' + i18n.txt.gender.before() + ' -',
#          '<b>' + create_gender_string(gender=gender_, i18n=i18n) + '</b>']) if gender_ else ''
#
#     if new_line:
#         name = name.capitalize() if name else name
#     age = age.capitalize() if age and not name else age
#     gender = gender.capitalize() if not name and not age else gender
#
#     str_list = [s for s in [name, age, gender] if s]
#
#     return ', '.join(str_list)
#
#
# def create_after_years_string(years: int, i18n: TranslatorRunner) -> str:
#     if (2 <= years % 10 <= 4) and not (10 <= years % 100 <= 20):
#         return i18n.txt.yearsstring2()
#     elif years % 10 == 1 and years % 100 != 11:
#         return i18n.txt.yearsstring1()
#     else:
#         return i18n.txt.yearsstring3()
#
#
# def create_gender_string(gender: Gender, i18n: TranslatorRunner) -> str:
#     if gender == Gender.male:
#         return i18n.txt.gender.male()
#     else:
#         return i18n.txt.gender.femail()
