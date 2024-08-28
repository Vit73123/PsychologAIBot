from logging import getLogger

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import async_sessionmaker

from tgbot.db.repo import Repo
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def set_user(message: Message, **kwargs) -> None:
    session: async_sessionmaker = kwargs.get('session')
    repo: Repo = kwargs.get('repo')
    state: FSMContext = kwargs.get('state')

    tg_user: types.User = message.from_user
    log.info(" Set user: %s", tg_user)

    user = await repo.user.get_user_by_user_id(session, tg_user.id)
    if not user:
        user = await repo.user.insert_user(session, tg_user)
    await state.update_data({'username': user.name})

    log.info(" state: %s", await state.get_data())

