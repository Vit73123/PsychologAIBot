from logging import getLogger
from typing import TYPE_CHECKING

from fluentogram import TranslatorRunner

from tgbot.db.dao import UserDAO
from tgbot.db.models.user import Gender
from tgbot.tools.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def create_aboutme_string(user: UserDAO, user_upd: UserDAO, i18n: TranslatorRunner) -> str:
    name_: str = user.name if not user_upd.name else user_upd.name
    age_: int = user.age if not user_upd.age else user_upd.age
    gender_: Gender = user.gender if not user_upd.gender else user_upd.gender

    name = ' '.join([i18n.txt.name.before(), '<b>' + name_ + '</b>']) if name_ else ''
    age: str = ' '.join(
        [i18n.txt.age.before(), '<b>' + str(age_) + '</b>', _after_years_string(years=age_, i18n=i18n)]) if age_ else ''
    gender: str = ' '.join([i18n.txt.gender.before(), '<b>' + get_gender_string(gender_) + '</b>']) if gender_ else ''

    str_list = [s for s in [name, age, gender] if s]

    return ' '.join(str_list)


def _after_years_string(years: int, i18n: TranslatorRunner) -> str:
    if (2 <= years % 10 <= 4) and not (10 <= years % 100 <= 20):
        return i18n.txt.yearsstring2()
    elif years % 10 == 1 and years % 100 != 11:
        return i18n.txt.yearsstring1()
    else:
        return i18n.txt.yearsstring3()


def get_gender_string(gender: Gender, i18n: TranslatorRunner) -> str:
    if Gender.male:
        return i18n.txt.gender.male()
    else:
        return i18n.txt.gender.femail()