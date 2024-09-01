from typing import Any

from aiogram import types

from tgbot.db.models import User
from tgbot.errors.errors import *
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def create_from_bot_user(bot_user: types.User) -> User:
    return User(
        user_id=bot_user.id,
        username=bot_user.username,
        first_name=bot_user.first_name,
        last_name=bot_user.last_name,
    )


def check_user_id(obj: Any, user_id: int, source: str):
    if obj and obj.user_id != user_id:
        raise UserIdError(source)
