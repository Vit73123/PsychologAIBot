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
    log.debug(' /status_g: get status id=1')

    status_id = 1

    # Получить состояние пользователя по id состояния
    status = await repo.status.get(status_id)

    log.debug(' /status_g: status: %s', status)


@router.message(Command(commands='status_gl'), IsAdmin())
async def cmd_get_last_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_gl: get last status: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Получить последнее состояние данного пользователя по его user_id в базе данных
    status = await repo.status.get_last_by_user_id(user_id)

    log.debug(' /status_gl: status: %s', status)


@router.message(Command(commands='status_a'), IsAdmin())
async def cmd_add_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log_dev.debug(' /status_a: add status: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    status = Status()
    status.user_id = user_id
    status.text = "New status"
    status.grade = 5

    # Добавить состояние для данного пользователя по его user_id
    await repo.status.add(status)

    db_status = await repo.status.get_last_by_user_id(user_id)
    log_dev.debug(' /status_a: status: %s', db_status)


@router.message(Command(commands='status_u'), IsAdmin())
async def cmd_update_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log_dev.debug(' /status_u: update id=1: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    status = Status()
    status.id = 1
    status.user_id = user_id
    status.text = "Updated status"
    status.grade = -5

    await repo.status.update(status)
    log_dev.debug(' /status_u: status: %s', await repo.status.get_last_by_user_id(user_id))


@router.message(Command(commands='status_d'))
async def cmd_delete_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_d: delete: id=1: from_user: %s', message.from_user)

    # data = await state.get_data()
    # status_id = data['status_id']
    status_id = 1

    await repo.status.delete(status_id)
