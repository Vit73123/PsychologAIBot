from tgbot.config.config import DBConfig
from .dto.db import DbDTO
from .repo.db import DbRepo


def create_db(db_config: DBConfig):
    repo = create_repo(db_config)
    return DbDTO(repo)


def create_repo(db_config: DBConfig):
    return DbRepo(db_config)
