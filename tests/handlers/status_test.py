from logging import getLogger

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.db import Status
from tgbot.db.repo import Repo
from tgbot.filters import *
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command(commands='status_g'), IsAdmin())
async def cmd_get_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_g: get status by id')

    id_ = 1
    log.debug(' /status_g: status id=%s', id_)

    status = await repo.status.get(id_)

    log.debug(' /status_g: status: %s', status)


@router.message(Command(commands='status_gl'), IsAdmin())
async def cmd_get_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_gl: get last status by user: %s', message.from_user)

    # data = state.get_data()
    # id_ = data['user_id']
    user_id = 1

    log.debug(' /status_gl: user id=%s', user_id)

    status = await repo.status.get_last_by_user_id(user_id)

    log.debug(' /status_gl: status: %s', status)


@router.message(Command(commands='status_a'), IsAdmin())
async def cmd_add_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log_dev.debug(' /status_a: add status by user: %s', message.from_user)

    # data = state.get_data()
    # id_ = data['user_id']
    user_id = 1

    log_dev.debug(' /status_a: user id=%s', message.from_user)

    status = Status()
    status.user_id = user_id
    status.text = "New status"
    status.grade = 5

    await repo.status.add(status)

    db_status = await repo.status.get_last_by_user_id(user_id)
    log_dev.debug(' /status_a: status: %s', db_status)


@router.message(Command(commands='status_u'), IsAdmin())
async def cmd_update_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log_dev.debug(' /status_u: update: from_user: %s', message.from_user)

    # data = state.get_data()
    # id_ = data['user_id']
    user_id = 1

    log_dev.debug(' /status_u: user id=%s', user_id)

    status = Status()
    status.id = 4
    status.user_id = user_id
    status.text = "Updated status"
    status.grade = -5

    await repo.status.update(status)
    log_dev.debug(' /status_u: status: %s', await repo.status.get_last_by_user_id(user_id))

# @router.message(Command(commands='status_d'))
# async def cmd_delete_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
#     log.debug(' /status_d: delete user: from_user: %s', message.from_user)
#
#     data = await state.get_data()
#     id_ = data['user_id']
#     await repo.user.delete(id_)
#
#
