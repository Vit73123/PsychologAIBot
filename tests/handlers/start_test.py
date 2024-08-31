import logging
from pprint import pprint

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncEngine

from tests.dialogs.states import Start
from tgbot.config.config import Config
from tgbot.db.factory import create_tables
from tgbot.db.repo import Repo
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.user_utils import create_from_bot_user

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, state: FSMContext, repo: Repo, **kwargs):
    log.debug(' /start')

    data = await state.get_data()
    if not data:
        user = create_from_bot_user(message.from_user)
        user = await repo.user.set(user)
        await state.set_data({'user_id': user.id})

    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)

@router.message(Command(commands='ct'))
async def cmd_create_tables_test(message: Message, engine: AsyncEngine, config: Config, **kwargs):
    log.debug(' /ct: create tables')
    await create_tables(engine, config.db)


@router.message(Command(commands='st'))
async def cmd_state_test(message: Message, state: FSMContext, **kwargs):
    log.debug(' /st: state: %s', await state.get_data())


@router.message(Command(commands='kw'))
async def cmd_kwargs_test(message: Message, **kwargs):
    log.debug(' /kw: context: %s')
    pprint(kwargs)
