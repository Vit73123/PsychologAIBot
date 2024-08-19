import logging
from pathlib import Path

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from tgbot.services.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command(commands='i'))
async def cmd_load_image(message: Message):
    log_dev.debug('/i')
    params = message.text.split(' ')
    log_dev.debug(Path('resources/images') / params[1])
    data = await message.answer_photo(
        photo=FSInputFile(Path('resources/images/') / params[1])
    )
    log_dev.debug(data.photo[-1].file_id)


@router.message(Command(commands='c'))
async def cmd_load_image(message: Message):
    log_dev.debug('/c')
    file_id = message.text.split(' ')[-1]
    data = await message.answer_photo(
        photo=file_id
    )
    log_dev.debug(data.photo[-1].file_id)
