from logging import getLogger
from typing import Any

from aiogram.fsm.context import FSMContext

from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_state_data(key: str, state: FSMContext) -> Any:
    state_data = await state.get_data()
    log_dev.debug(" get_state_data: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())
    return state_data[key]


async def reset_fsm(state: FSMContext, persistent_context_names: list[str] = None) -> None:
# async def reset_fsm(state: FSMContext, persistent_context_names: list[str] = None) -> dict:
    if not persistent_context_names:
        persistent_context_names = ['user_data']

    contexts_bak: list[dict] = []
    state_data = await state.get_data()

    for name in persistent_context_names:
        contexts_bak.append({
            name: state_data[name]
        })

    await state.set_data({})

    for context in contexts_bak:
        await state.update_data(context)