from tgbot.db.models import User
from aiogram.types import User as TgUser


def to_user(tg_user: TgUser):
    return User(
        user_id=tg_user.id,
        username=tg_user.username,
        first_name=tg_user.first_name,
        last_name=tg_user.last_name,
    )
