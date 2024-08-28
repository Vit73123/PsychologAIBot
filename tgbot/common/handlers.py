from logging import getLogger

from aiogram import types

from tgbot.db.queries import (
    get_user_by_user_id,
    insert_user
)
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def set_user(session: dict, tg_user: types.User) -> None:
    log.info(" Set user: %s", tg_user)

    session_pool = session['session_pool']
    user = await get_user_by_user_id(session_pool, tg_user.id)
    if not user:
        user = await insert_user(session_pool, tg_user)
    session['user_data'] = {'username': user.name}
