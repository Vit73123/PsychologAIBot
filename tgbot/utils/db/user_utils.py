from tgbot.db.dao import UserDAO
from tgbot.db.models import User
from tgbot.errors.errors import *
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def create_user_from_bot(bot_user) -> User:
    return User(
        user_id=bot_user.id,
        username=bot_user.username,
        first_name=bot_user.first_name,
        last_name=bot_user.last_name,
    )


def create_user_to_dao(user: User) -> UserDAO | None:
    if user:
        return UserDAO(
            user_id=user.id,
            name=user.name,
            gender=user.gender,
            age=user.age
        )


def create_user_from_dao(user_dao: UserDAO) -> User | None:
    if user_dao:
        user = User()
        user.id = user_dao.id
        user.name = user_dao.name
        user.gender = user_dao.gender
        user.age = user_dao.age
        return user

# def create_user_name_text(name: str, i18n: TranslatorRunner) -> str:
#     return escape_text(
#         i18n.txt.name.anonim() if not name else name
#     )
