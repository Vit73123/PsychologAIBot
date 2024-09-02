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


@router.message(Command(commands='user_reg'), IsAdmin())
async def cmd_set_test(message: Message, dialog_manager: DialogManager, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /user_reg: register user: state: %s, from_user: %s', await state.get_data(), message.from_user)

    data = await state.get_data()

    if not data:
        user: User = create_user_from_bot(message.from_user)

        # Регистрация пользователя
        user: UserDAO = await repo.user.register(user)

        # Сохранить в общий контекст локальный id пользователя из базы данных
        await state.set_data({'user_id': user.id})

        log.debug(' /user_reg: state: %s, user: %s', await state.get_data(), user)


@router.message(Command(commands='user_g'), IsAdmin())
async def cmd_get_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /user_g: get user: state: %s', await state.get_data())

    # data = await state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Получить пользователя по id базы данных (из общего контекста бота)
    user: User = await repo.user.get(user_id)

    log.debug(' /user_g: user: %s', user)


@router.message(Command(commands='user_gg'), IsAdmin())
async def cmd_get_by_bot_user_id_test(message: Message, repo: Repo, **kwargs):
    log.debug(' /user_gg: get user: bot_user_id=1111111111')

    user_id = 1111111111

    # Получить пользователя по user_id телеграмма
    user = await repo.user.get_by_bot_user_id(user_id)

    log.debug(' /user_gg: user: %s', user)


@router.message(Command(commands='user_ga'), IsAdmin())
async def cmd_get_with_all_statuses_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log.debug(' /user_ga: get with all statuses by user id=1: from_user: %s', message.from_user)

    # data = await state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Получить пользователя и все его статусы, отсортированные по убыванию даты
    user = await repo.user._get_with_all_statuses_to_user(user_id)

    log.debug(' /user_ga: user: %s', user)
    log.debug(' /user_ga: statuses: %s', user.statuses)


@router.message(Command(commands='user_a'), IsAdmin())
async def cmd_add_test(message: Message, repo: Repo, **kwargs):
    log.debug(" /user_a: add user "
              "user_id=9999999999 "
              "username='New user name' "
              "first_name='New first name' "
              "last_name='New last name'")

    user = User()
    user.user_id = 9999999999
    user.username = 'New user name'
    user.first_name = 'New first name'
    user.last_name = 'New last name'

    # Добавить нового пользователя
    await repo.user._add(user)


@router.message(Command(commands='user_u'), IsAdmin())
async def cmd_update_test(message: Message, state: FSMContext, repo: Repo, **kwargs):
    log.debug(' /user_u: update user id=1, name=Vladimir')

    # data = await state.get_data()
    # user.id = data['user_id']
    user = UserDAO(
        user_id=1,
        name="Vladimir"
    )

    # Изменить пользователя
    await repo.user.update(user)

    log.debug(' /user_u: user: %s', await repo.user.get(user.id))


@router.message(Command(commands='user_d'), IsAdmin())
async def cmd_delete_test(message: Message, repo: Repo, state: FSMContext, **kwargs):
    log.debug(' /user_d: delete user id=1: from_user: %s', message.from_user)

    # data = await state.get_data()
    # user_id = data['user_id']
    user_id = 1

    # Удалить пользователя
    await repo.user.delete(user_id)
