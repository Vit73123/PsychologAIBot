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
from tgbot.filters import IsAdmin
from tgbot.utils.user_utils import *

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, state: FSMContext, repo: Repo, **kwargs):
    log.debug(' /start')

    data = await state.get_data()

    # Регистрация пользователя: добавить в общий контекст бота его id из базы данных
    if not data:
        user = create_from_bot_user(message.from_user)
        user = await repo.user.set(user)
        await state.set_data({'user_id': user.id})

    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='start_'), IsAdmin())
async def cmd_start(message: Message, state: FSMContext, **kwargs):
    log.debug(' /start_')

    await message.answer(text="""
    Команды-эндпоинты api бота
    
    /start    - start bot: Регистрация Диалог start
    /start_   - это сообщение
    
    /ct       - create tables
    /st       - bot state data
    /kw       - bot context (kwargs)
    
    /user_start - start bot: регистрация пользователя
    /user_g   - get user id=1
    /user_gg  - get user by bot user bot_id=XXX
    /user_a   - add user id=1
    /user_d   - delete user id=1
    /user_u   - update user id=1
    /user_s   - get user with all statuses id=1 
    
    /status_g  - get status id=1
    /status_gl - get last status by user_id=1
    /status_a  - add status id=1
    /status_d  - delete status id=1
    /status_u  - update status id=1
    """)


@router.message(Command(commands='ct'), IsAdmin())
async def cmd_create_tables_test(message: Message, state: FSMContext, engine: AsyncEngine, config: Config, **kwargs):
    log.debug(" /ct: create tables")

    await create_tables(engine, config.db)


@router.message(Command(commands='st'), IsAdmin())
async def cmd_state_test(message: Message, state: FSMContext, **kwargs):
    log.debug(" /st: state: %s", await state.get_data())


@router.message(Command(commands='kw'), IsAdmin())
async def cmd_kwargs_test(message: Message, state: FSMContext, **kwargs):
    log.debug(' /kw: context: %s')

    pprint(kwargs)
