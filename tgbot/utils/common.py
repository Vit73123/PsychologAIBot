from typing import Any

from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner

from tgbot.db.models.user import Gender


async def get_state_data(key: str, state: FSMContext) -> Any:
    state = await state.get_data()
    return state.get(key)


def create_after_years_string(years: int, i18n: TranslatorRunner) -> str:
    if (2 <= years % 10 <= 4) and not (10 <= years % 100 <= 20):
        return i18n.txt.yearsstring2()
    elif years % 10 == 1 and years % 100 != 11:
        return i18n.txt.yearsstring1()
    else:
        return i18n.txt.yearsstring3()


def create_gender_string(gender: Gender, i18n: TranslatorRunner) -> str:
    if gender == Gender.male:
        return i18n.txt.gender.male()
    else:
        return i18n.txt.gender.femail()
