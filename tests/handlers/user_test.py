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


@router.message(Command(commands='user-start'))
async def cmd_start_test(message: Message, dialog_manager: DialogManager, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /us: start from_user: %s', message.from_user)
    log.debug(' /us: state data: %s', await state.get_data())

    data = await state.get_data()

    if not data:
        user = create_from_bot_user(message.from_user)

        log.debug(' /us: bot start: user: %s', user)

        user = await repo.user.set(user)
        await state.set_data({'user_id': user.id})
        log.debug(' /us: user: %s', user)

    log.debug(' /us: state: %s', await state.get_data())


@router.message(Command(commands='user-g'))
async def cmd_get_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /ug: get user: state: %s', await state.get_data())

    data = await state.get_data()
    id_ = data['user_id']

    log.debug(' /ug: user id=%s', id_)

    user = await repo.user.get(id_)

    log.debug(' /ug: user: %s', user)


@router.message(Command(commands='user-gg'))
async def cmd_get_by_user_id_test(message: Message, repo: Repo, **kwargs):
    log.debug(' /ugg: get user: from user_id=%s', message.from_user.id)

    user = await repo.user.get_by_bot_user_id(message.from_user.id)

    log.debug(' /ugg: user: %s', user)


@router.message(Command(commands='user-a'))
async def cmd_add_test(message: Message, repo: Repo, **kwargs):
    log.debug(' /ua: add user: from_user: %s', message.from_user)

    user = create_from_bot_user(message.from_user)
    await repo.user.add(user)


@router.message(Command(commands='user-d'))
async def cmd_delete_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /ud: delete user: from_user: %s', message.from_user)

    data = await state.get_data()
    id_ = data['user_id']
    await repo.user.delete(id_)


@router.message(Command(commands='user-u'))
async def cmd_update_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log.debug(' /uu: update: from_user: %s', message.from_user)

    user = create_from_bot_user(message.from_user)
    log.debug(' /uu: user id=%s name=%s', user.id, user.name)

    data = await state.get_data()
    user.id = data['user_id']

    user.name = "Vladimir"
    log.debug(' /uu: user id=%s name=%s', user.id, user.name)

    await repo.user.update(user)
    log.debug(' /uu: user: %s', await repo.user.get(user.id))


@router.message(Command(commands='user-gs'))
async def cmd_get_with_statuses_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log_dev.debug(' /ugs: get with statuses: from_user: %s', message.from_user)

    data = await state.get_data()
    id_ = data['user_id']

    log_dev.debug(' /ugs: user id=%s', id_)

    user_statuses = await repo.user.get_with_statuses(id_)

    log_dev.debug(' /ugs: user statuses: %s', user_statuses)
