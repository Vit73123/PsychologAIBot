from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.errors.errors import *
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class IsAdmin(BaseFilter):
    admin_ids: list[int]

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in IsAdmin.admin_ids
