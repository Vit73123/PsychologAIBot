from tgbot.config.config import DBConfig
from .repo.db import DbRepo


def create_repo(db_config: DBConfig):
    return DbRepo(db_config)
