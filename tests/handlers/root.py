import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from tests.dialogs.states import Start
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

    await dialog_manager.start(state=Start.start, mode=StartMode.RESET_STACK)


@router.message(Command(commands='c'))
async def cmd_dialog_1(message: Message, dialog_manager: DialogManager, db: DbService, **kwargs):
    log.info(' /c: create tables')
    await db.create_tables()


@router.message(Command(commands='a'))
async def cmd_dialog_1(message: Message, dialog_manager: DialogManager, db: DbService, **kwargs):
    log.info(' /a: insert user: %s', message.from_user)

    # await db.user.insert_user(message.from_user)
