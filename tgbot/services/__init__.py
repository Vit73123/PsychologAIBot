from tgbot.config.config import DBConfig
from tgbot.db import create_repo
from .db.db import DbService
from .locales import i18n

def create_db(db_config: DBConfig):
    repo = create_repo(db_config)
    return DbService(repo)
