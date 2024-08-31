import logging
from pprint import pprint

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager

from tgbot.db.models import User
from tgbot.services import DbService
from tgbot.utils.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, dialog_manager: DialogManager, **kwargs):
    log.info(' /start')
    state: FSMContext = kwargs.get("state")
    data = await state.get_data()
    log.info(' state: %s', data)
    # pprint(kwargs)                  # Вывести весь контекст бота

    # await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='s'))
async def cmd_start(message: Message, dialog_manager: DialogManager, db: DbService, state: FSMContext, **kwargs):
    log.info(' /s: start')
    data = await state.get_data()

    if not data:
        user = await db.user.set(message.from_user)
        await state.set_data({'user_id': user.id})


@router.message(Command(commands='g'))
async def cmd_get(message: Message, db: DbService, state: FSMContext, **kwargs):
    log.info(' /g: get by user id')

    data = await state.get_data()
    id_ = data['user_id']
    user = await db.user.get(id_)
    log.debug(' user: %s', user)


@router.message(Command(commands='gg'))
async def cmd_get(message: Message, db: DbService, **kwargs):
    log.info(' /gg: get by bot user id')

    user = await db.user._get_by_bot_user_id(message.from_user.id)
    log_dev.info(' user: %s', user)


@router.message(Command(commands='a'))
async def cmd_insert(message: Message, db: DbService, **kwargs):
    log.info(' /a: add by bot user')

    await db.user.add(message.from_user)


@router.message(Command(commands='u'))
async def cmd_update(message: Message, db: DbService, **kwargs):
    log.info(' /u: update by user')

    user = User()
    user.name = "Vladimir"
    await db.user.update(user)


@router.message(Command(commands='ct'))
async def cmd_dialog_1(message: Message, db: DbService, **kwargs):
    log.info(' /ct: create tables')
    await db.create_tables()


@router.message(Command(commands='dt'))
async def cmd_update(message: Message, state: FSMContext, **kwargs):
    log.info(' /dt: state data (state.get_data): %s', await state.get_data())


@router.message(Command(commands='kw'))
async def cmd_update(message: Message, **kwargs):
    log.info(' /kw: context (kwargs): %s')
    pprint(kwargs)
