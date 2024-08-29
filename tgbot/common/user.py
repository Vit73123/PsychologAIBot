from logging import getLogger
from pprint import pprint

from aiogram import types
from aiogram.fsm.context import FSMContext

from tgbot.db import Repo
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def set_user(tg_user: types.User, **kwargs) -> None:
    log.info(" Set user: %s", tg_user)

    repo: Repo = kwargs.get('repo')
    state: FSMContext = kwargs.get('state')
    data = await state.get_data()

    user = await repo.user.get_user_by_user_id(tg_user.id)
    if not user:
        user = await repo.user.insert_user(tg_user)
    await state.update_data({'username': user.name})

    log.info(" state: %s", await state.get_data())
