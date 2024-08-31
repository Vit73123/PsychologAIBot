from logging import getLogger

from aiogram import types

from tgbot.db.models import User
from tgbot.db.repo.user import UserRepo
from tgbot.utils.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class UserService:
    _repo: UserRepo

    def __init__(self, repo: UserRepo):
        self._repo = repo

    async def get(self, id_: int) -> User:
        log_dev.debug(" Db: get user id=%s", id_)

        return await self._repo.get(id_)

    async def add(self, bot_user: types.User) -> User:
        log.debug(" Db: add bot user: %s", bot_user)

        user: User = self._create_from_bot_user(bot_user)
        return await self._repo.add(user)

    async def update(self, user: User) -> None:
        log_dev.debug(" Db: update user data: %s", data)

        log_dev.debug(" User fields: %s", User._fields)

        # user = User()
        # for item in data:
        #     "user_id={self.user_id} "
        #     f"username={self.username} "
        #     f"first_name={self.first_name} "
        #     f"last_name={self.last_name} "
        #     f"name={self.name} "
        #     f"gender={self.gender} "
        #     f"age={self.age} "
        #     f"created_at={self.created_at} "
        #     f"updated_at={self.updated_at}")
        #
        #
        #
        #     user: User = self._create_from_bot_user(bot_user)
        # await self._repo.add(user)

    async def set(self, bot_user: types.User) -> User:
        log.debug(" Db: set user by bot user: %s", bot_user)

        user: User = self._create_from_bot_user(bot_user)
        user_db = await self._repo.get_by_bot_user_id(bot_user.id)
        if not user_db:
            user.id = await self._repo.add(user)
        elif user != user_db:
            log_dev.fatal(" Db: Corrupted user: should be updated!")
        else:
            user.id = user_db.id
        log_dev.debug(" Db: user: %s", user)
        return user

    async def _get_by_bot_user_id(self, bot_user_id: int) -> User:
        log.debug(" Db: get user by bot user id=%s", bot_user_id)

        return await self._repo.get_by_bot_user_id(bot_user_id)

    def _create_from_bot_user(self, bot_user: types.User) -> User:
        return User(
            user_id=bot_user.id,
            username=bot_user.username,
            first_name=bot_user.first_name,
            last_name=bot_user.last_name,
        )
