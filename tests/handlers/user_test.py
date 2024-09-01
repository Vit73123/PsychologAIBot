import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_dialog import DialogManager

from tgbot.db.repo import Repo
from tgbot.filters import IsAdmin
from tgbot.utils.user_utils import *

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

router = Router()


@router.message(Command(commands='user_start'), IsAdmin())
async def cmd_start_test(message: Message, dialog_manager: DialogManager, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /user_start: start from_user: %s', message.from_user)

    data = await state.get_data()

    if not data:
        user = create_from_bot_user(message.from_user)

        # Регистрация пользователя
        user = await repo.user.set(user)

        # Сохранить в общий контекст локальный id пользователя из базы данных
        await state.set_data({'user_id': user.id})

    log.debug(' /user_start: state: %s', await state.get_data())


@router.message(Command(commands='user_g'), IsAdmin())
async def cmd_get_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /user_g: get user: state: %s', await state.get_data())

    # data = await state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Получить пользователя по id базы данных (из общего контекста бота)
    user = await repo.user.get(user_id)

    log.debug(' /user_g: user: %s', user)


@router.message(Command(commands='user_gg'), IsAdmin())
async def cmd_get_by_bot_user_id_test(message: Message, repo: Repo, **kwargs):
    log.debug(' /user_gg: get user: bot_user_id=%s', message.from_user.id)

    # Получить пользователя по user_id телеграмма
    user = await repo.user.get_by_bot_user_id(message.from_user.id)

    log.debug(' /user_gg: user: %s', user)


@router.message(Command(commands='user_a'), IsAdmin())
async def cmd_add_test(message: Message, repo: Repo, **kwargs):
    log.debug(' /user_a: add bot user: %s', message.from_user)

    user = create_from_bot_user(message.from_user)

    # Добавить нового пользователя
    await repo.user.add(user)


@router.message(Command(commands='user_d'), IsAdmin())
async def cmd_delete_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /user_d: delete bot user: %s', message.from_user)

    # data = await state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Удалить пользователя
    await repo.user.delete(user_id)


@router.message(Command(commands='user_u'), IsAdmin())
async def cmd_update_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log.debug(' /user_u: update bot user: %s', message.from_user)

    user = create_from_bot_user(message.from_user)

    # data = await state.get_data()
    # user.id = data['user_id']
    user.id = 1
    user.name = "Vladimir"

    # Изменить пользователя
    await repo.user.update(user)

    log.debug(' /user_u: user: %s', await repo.user.get(user.id))


@router.message(Command(commands='user_s'), IsAdmin())
async def cmd_get_with_all_statuses_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log.debug(' /user_s: get with all statuses: from user: %s', message.from_user)

    # data = await state.get_data()
    # user_id = data['user_id']
    user_id = 1

    log.debug(' /user_ls: user id=%s', user_id)

    # Получить пользователя и все его статусы, отсортированные по убыванию даты
    user = await repo.user.get_with_all_statuses(user_id)

    log.debug(' /user_ls: user: %s', user)
    log.debug(' /user_ls: statuses: %s', user.statuses)
