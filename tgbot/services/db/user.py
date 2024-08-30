from logging import getLogger

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import User as BotUser

from tgbot.db.models import User
from tgbot.db.repo.user import UserRepo
from tgbot.utils.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class UserService:
    _repo: UserRepo

    def __init__(self, repo: UserRepo):
        self._repo = repo

    async def insert_user(self, bot_user: types.User):
        log_dev.info(" insert bot_user: %s", bot_user)

        user: User = self.from_bot_user(bot_user)
        log_dev.info(" to user: %s", user)


    async def create_user(self, bot_user: types.User, **kwargs) -> None:
        log.info(" set new user: %s", bot_user)

        state: FSMContext = kwargs.get('state')
        data = await state.get_data()

        user = await self._repo.get_user_by_user_id(bot_user.id)
        if not user:
            user = await self._repo.insert_user(bot_user)
        await state.update_data({'username': user.name})

        log.info(" start handler: state: %s", await state.get_data())

    def from_bot_user(self, bot_user: BotUser):
        return User(
            user_id=bot_user.id,
            username=bot_user.username,
            first_name=bot_user.first_name,
            last_name=bot_user.last_name,
        )
