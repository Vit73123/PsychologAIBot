from logging import getLogger

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.db.dao import StatusDAO
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
    status: StatusDAO = await repo.status.get(status_id)

    log.debug(' /status_g: status: %s', status)


@router.message(Command(commands='status_gl'), IsAdmin())
async def cmd_get_last_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_gl: get last status: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Получить последнее состояние данного пользователя по его user_id в базе данных
    status: StatusDAO = await repo.status.get_last_by_user_id(user_id)

    log.debug(' /status_gl: status: %s', status)


@router.message(Command(commands='status_ga'), IsAdmin())
async def cmd_get_all_by_user_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_ga: get all statuses: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Получить все состояния данного пользователя по его user_id в базе данных
    statuses: list[StatusDAO] = await repo.status.get_all_by_user_id(user_id)

    log.debug(' /status_ga: statuses: %s', statuses)


@router.message(Command(commands='status_a'), IsAdmin())
async def cmd_add_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log_dev.debug(' /status_a: add status: from_user: %s', message.from_user)

    # data = state.get_data()
    # user_id = data['user_id']
    user_id = 1

    status = StatusDAO(
        text="New status",
        grade=5,
        user_id=user_id
    )

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

    status = StatusDAO(
        status_id=1,
        user_id=user_id,
        text="Updated status",
        grade=-5
    )

    # Изменить состояние
    await repo.status.update(status)
    log_dev.debug(' /status_u: status: %s', await repo.status.get_last_by_user_id(user_id))


@router.message(Command(commands='status_d'))
async def cmd_delete_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_d: delete: id=1: from_user: %s', message.from_user)

    # data = await state.get_data()
    # status_id = data['status_id']
    status_id = 1

    # Удалить состояние
    await repo.status.delete(status_id)


@router.message(Command(commands='status_dl'))
async def cmd_delete_last_by_user_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_dl: delete last: from_user: %s', message.from_user)

    # data = await state.get_data()
    # status_id = data['status_id']
    user_id = 1

    # Удалить последнее состояние данного пользователя по его user_id в базе данных
    await repo.status.delete_last_by_user_id(user_id)


@router.message(Command(commands='status_da'))
async def cmd_delete_all_by_user_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /status_da: delete all: from_user: %s', message.from_user)

    # data = await state.get_data()
    # status_id = data['status_id']
    user_id = 1

    # Удалить все состояния данного пользователя по его user_id
    await repo.status.delete_all_by_user(user_id)
