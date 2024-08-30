from tgbot.db import create_repo


def create_db(db_config: DBConfig):
    return Repo(db_config)