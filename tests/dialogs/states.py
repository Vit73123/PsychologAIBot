from aiogram.fsm.state import StatesGroup, State


class Start(StatesGroup):
    start = State()


class Dialog_1(StatesGroup):
    dialog_1 = State()
