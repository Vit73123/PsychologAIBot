from logging import getLogger

from fluentogram import TranslatorRunner

from tgbot.db.models.user import Gender
from tgbot.tools.jinja import escape_text
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# Имя
def create_name_string(name: str) -> str:
    """
    Получить строку имени
    Если name=None, то вернуть пустую строку

    :param name:
    :return:
    """
    return name if name else ''


def create_show_name_string(name: str, i18n: TranslatorRunner) -> str:
    """
    Получить имя пользователя
    Если пользователь анонимный name=None, то вернуть общее имя анонимного пользователя

    :param name:
    :param i18n:
    :return:
    """
    return escape_text(
        i18n.txt.name.anonim() if not name else name
    )


# Возраст
def create_age_f_string(age: int, i18n: TranslatorRunner) -> str:
    """
    Получить строку возраста со словом лет после числа

    :param age:
    :param i18n:
    :return:
    """
    return ' '.join([str(age), create_after_years_string(years=age, i18n=i18n)]) if age else ''


def create_age_string(age: int) -> str:
    """
    Получить строку возраста из числа лет (только число)
    Если age=None, то вернуть пустую строку

    :param age:
    :return:
    """
    return str(age) if age else ''


# Пол
def create_gender_string(gender: Gender | None, i18n: TranslatorRunner) -> str:
    """
    Получить слово, соответствующее строковому обозначению пола человека

    :param gender:
    :param i18n:
    :return:
    """

    if gender:
        if gender == Gender.m:
            return i18n.txt.gender.male.long()
        else:
            return i18n.txt.gender.female.long()
    else:
        return ''


# Состояние
def create_status_string(name: str) -> str:
    """
    Получить строку имени
    Если name=None, то вернуть пустую строку

    :param name:
    :return:
    """
    return name if name else ''


# Оценка состояния
def create_grade_f_string(grade: int | str) -> str:
    """
    Получить строку оценки состояния с обязательным ведущим знаком: + -
    Если name=None, то вернуть пустую строку

    :param grade:
    :return:
    """
    return f"{int(grade):+}" if grade else ''


def create_grade_string(grade: int | str) -> str:
    """
    Получить строку оценки состояния
    Если name=None, то вернуть пустую строку

    :param grade:
    :return:
    """
    return str(grade) if grade else ''


# Строковые утилиты

def create_after_years_string(years: int, i18n: TranslatorRunner) -> str:
    """
    Добавить после числа лет слово (год, лет)

    :param years:
    :param i18n:
    :return:
    """
    if (2 <= years % 10 <= 4) and not (10 <= years % 100 <= 20):
        return i18n.txt.yearsstring2()
    elif years % 10 == 1 and years % 100 != 11:
        return i18n.txt.yearsstring1()
    else:
        return i18n.txt.yearsstring3()


def lower_string(text: str):
    """
    Сделать первую букву строки в нижнем регистре

    :param text:
    :return:
    """
    return text[0].lower() + text[1:]
