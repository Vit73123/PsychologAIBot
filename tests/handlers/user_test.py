import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager

from tgbot.db.repo import Repo
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.user_utils import create_from_bot_user

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command(commands='s'))
async def cmd_start_test(message: Message, dialog_manager: DialogManager, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /s: start from_user: %s', message.from_user)
    log.debug(' /s: state data: %s', await state.get_data())

    data = await state.get_data()

    if not data:
        user = create_from_bot_user(message.from_user)

        log.debug(' /s: bot start: user: %s', user)

        user = await repo.user.set(user)
        await state.set_data({'user_id': user.user_id})
        log.debug(' /s: user: %s', user)

    log.debug(' /s: state: %s', await state.get_data())


@router.message(Command(commands='g'))
async def cmd_get_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /g: get user: state: %s', await state.get_data())

    data = await state.get_data()
    id_ = data['user_id']

    log.debug(' /g: user id: %s', id_)

    user = await repo.user.get(id_)

    log.debug(' /g: user: %s', user)


@router.message(Command(commands='gg'))
async def cmd_get_by_user_id_test(message: Message, repo: Repo, **kwargs):
    log.debug(' /gg: get user: from user_id=%s', message.from_user.id)

    user = await repo.user.get_by_bot_user_id(message.from_user.id)

    log.debug(' /gg: user: %s', user)


@router.message(Command(commands='a'))
async def cmd_add_test(message: Message, repo: Repo, **kwargs):
    log.debug(' /a: add user: from_user: %s', message.from_user)

    user = create_from_bot_user(message.from_user)
    await repo.user.add(user)


@router.message(Command(commands='u'))
async def cmd_update_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log.debug(' /u: update: from_user: %s', message.from_user)
    user = create_from_bot_user(message.from_user)
    log.debug(' /u: user id=%s name=%s', user.id, user.name)

    user.name = "Vladimir"
    data = await state.get_data()
    user.id = data['user_id']
    log.debug(' /u: user id=%s name=%s', user.id, user.name)

    await repo.user.update(user)
    log.debug(' /u: user: %s', await repo.user.get(user.id))
