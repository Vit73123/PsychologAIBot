from logging import getLogger

from aiogram import types

from tgbot.db.models import User
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def create_from_bot_status(bot_user: types.User) -> User:
    return User(
        user_id=bot_user.id,
        username=bot_user.username,
        first_name=bot_user.first_name,
        last_name=bot_user.last_name,
    )
