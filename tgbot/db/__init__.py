from tgbot.config.config import DBConfig
from .repo.repo import Repo


def create_repo(db_config: DBConfig):
    return Repo(db_config)
