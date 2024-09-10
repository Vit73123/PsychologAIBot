import logging
from pprint import pprint
from typing import TYPE_CHECKING

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncEngine

from tgbot.config import Config
from tgbot.db.factory import create_tables
from tgbot.filters import IsAdmin
from tgbot.tools.logger import get_logger_dev
from tgbot.tools.main_menu import del_main_menu

if TYPE_CHECKING:
    pass

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command(commands='delmenu'), IsAdmin())
async def cmd_delete_main_menu(message: Message, bot: Bot, **kwargs):
    log.debug(" /delmenu: delete main menu")

    # pprint(kwargs)
    await del_main_menu(message=message, bot=bot)


@router.message(Command(commands='ct'), IsAdmin())
async def cmd_create_tables(message: Message, engine: AsyncEngine, config: Config, **kwargs):
    log.debug(" /ct: create tables")

    await create_tables(engine, config.db)
