import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from tgbot.services.logger import get_logger_sel
from tgbot.common import commands as cmd

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = logging.getLogger(__name__)
log_new = get_logger_sel(__name__, log.getEffectiveLevel())

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, i18n: TranslatorRunner):
    log.debug('/start')
    await message.answer(text=i18n.start(
        cmd_psychology='/psychology',
        cmd_tests='/tests',
        cmd_profile='/profile'
    ))
