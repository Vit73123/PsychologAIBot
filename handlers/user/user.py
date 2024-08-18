import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.logger import get_logger_new

log = logging.getLogger(__name__)
log_new = get_logger_new(__name__, log.getEffectiveLevel())

router = Router()


@router.message(CommandStart)
async def cmd_start(message: Message):
    log.debug('/start')
