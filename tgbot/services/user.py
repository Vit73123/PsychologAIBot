from logging import getLogger

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import User as BotUser

from tgbot.db import Repo
from tgbot.db.models import User
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def create_user(tg_user: types.User, **kwargs) -> None:
    log.info(" Set new user: %s", tg_user)

    repo: Repo = kwargs.get('repo')
    state: FSMContext = kwargs.get('state')
    data = await state.get_data()

    user = await repo.user.get_user_by_user_id(tg_user.id)
    if not user:
        user = await repo.user.insert_user(tg_user)
    await state.update_data({'username': user.name})

    log.info(" Start handler: state: %s", await state.get_data())


def get_from_bot_user(bot_user: BotUser):
    return User(
        user_id=bot_user.id,
        username=bot_user.username,
        first_name=bot_user.first_name,
        last_name=bot_user.last_name,
    )
