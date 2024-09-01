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
        user = await repo.user.set(user, message.from_user.id)
        await state.set_data({'user_id': user.id})

    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='start_'), IsAdmin())
async def cmd_start(message: Message, state: FSMContext, **kwargs):
    log.debug(' /start_')

    await message.answer(text="""
    Команды-эндпоинты api бота
    
    /start    - start bot: диалог start
    
    /ct       - create tables
    /st       - bot state data
    /kw       - bot context (kwargs)
    
    /user_start - start bot: регистрация пользователя
    /user_g   - get user
    /user_gg  - get user by bot user id
    /user_a   - add user 
    /user_d   - delete user
    /user_u   - update user
    /user_s   - get user with all statuses 
    
    /status_g  - get status
    /status_gl - get last status by user id
    /status_a  - add status 
    /status_d  - delete status
    /status_u  - update status
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
