import logging
from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncEngine

from tgbot.config import Config
from tgbot.db.factory import create_tables
from tgbot.filters import IsAdmin
from tgbot.tools.logger import get_logger_dev

if TYPE_CHECKING:
    pass

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command(commands='ct'), IsAdmin())
async def cmd_create_tables_test(message: Message, state: FSMContext, engine: AsyncEngine, config: Config, **kwargs):
    log.debug(" /ct: create tables")

    await create_tables(engine, config.db)
