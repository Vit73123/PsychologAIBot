import asyncio
import logging

from tests.test_db import run_db_tests
from tgbot.config.config import Config, load_config
from tgbot.db import create_repo
from tgbot.services.logger import LoggerFormatter, FORMAT

# Конфигурация логирования
logging.basicConfig(
    # level=logging.DEBUG,
    level=logging.INFO,
    handlers=[logging.StreamHandler(), logging.FileHandler('tgbot/log/my_test_log.log', 'w')]
)
logging.getLogger().handlers[0].setFormatter(LoggerFormatter())
logging.getLogger().handlers[1].setFormatter(logging.Formatter(FORMAT))

# Отключить дублирование логирования SQLAlchemy
from sqlalchemy import log as sqlalchemy_log

sqlalchemy_log._add_default_handler = lambda x: None

log = logging.getLogger(__name__)


async def main():
    config: Config = load_config()

    # Подключение к базе данных и создание репозитория
    repo = create_repo(config.db)

    # Создание таблиц
    if config.db.create_tables:
        await repo.create_tables()

    await run_db_tests(repo)


if __name__ == '__main__':
    asyncio.run(main())
