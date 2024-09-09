from fluentogram import TranslatorRunner

from tgbot.db.models.user import Gender


# Name
def create_name_string(name: str) -> str:
    return name if name else ''


# Age
def create_age_string(age: int) -> str:
    return str(age) if age else ''


def create_age_f_string(age: int, i18n: TranslatorRunner) -> str:
    return ' '.join([str(age), create_after_years_string(years=age, i18n=i18n)]) if age else ''


# Gender
def create_gender_f_string(gender: Gender, i18n: TranslatorRunner) -> str:
    if gender:
        if gender == Gender.male:
            return i18n.txt.gender.male()
        else:
            return i18n.txt.gender.femail()
    else:
        return ''


def create_gender_string(gender: Gender) -> str:
    return str(gender)


# Name
def create_status_string(name: str) -> str:
    return name if name else ''


# Grade
def create_grade_f_string(grade: int) -> str:
    return f"{grade:+}" if grade else ''


def create_grade_string(grade: int) -> str:
    return str(grade) if grade else ''


# years
def create_after_years_string(years: int, i18n: TranslatorRunner) -> str:
    if (2 <= years % 10 <= 4) and not (10 <= years % 100 <= 20):
        return i18n.txt.yearsstring2()
    elif years % 10 == 1 and years % 100 != 11:
        return i18n.txt.yearsstring1()
    else:
        return i18n.txt.yearsstring3()


# lower text
def lower_text(text: str):
    return text[0].lower() + text[1:]
