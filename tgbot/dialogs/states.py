from aiogram.fsm.state import StatesGroup, State


class Start(StatesGroup):
    start = State()
    dialog = State()


class Psychology(StatesGroup):
    start = State()
    appointment = State()
    review = State()


class Tests(StatesGroup):
    start = State()
    choose_test = State()
    test = State()


class Aboutme(StatesGroup):
    start = State()
    profile = State()
    data = State()
    name = State()
    age = State()
    gender = State()
    status = State()
    grade = State()
    yesno_name = State()
    yesno_age = State()
    yesno_gender = State()
    yesno_status = State()
    yesno_grade = State()
