from aiogram.fsm.state import StatesGroup, State


class Start(StatesGroup):
    start = State()
    psychology = State()


class Dialog_1(StatesGroup):
    start = State()
