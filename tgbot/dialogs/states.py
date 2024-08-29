from aiogram.fsm.state import StatesGroup, State


class Start(StatesGroup):
    start = State()


class Psychology(StatesGroup):
    start = State()
    session = State()


class Tests(StatesGroup):
    start = State()
    choose_test = State()
    test = State()


class Profile(StatesGroup):
    start = State()
    about_me = State()
