from typing import Any

from aiogram.fsm.context import FSMContext


async def get_state_data(key: str, state: FSMContext) -> Any:
    state = await state.get_data()
    return state.get(key)