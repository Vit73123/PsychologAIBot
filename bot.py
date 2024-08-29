import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from tgbot.config.config import Config, load_config
from tgbot.db import create_repo
from tgbot.dialogs import (
    start_dialog,
    psychology_dialog,
    tests_dialog,
    profile_dialog,
)
from tgbot.handlers.user.user import router as user_router
from tgbot.middlewares.i18n import TranslatorRunnerMiddleware
from tgbot.services.i18n import create_translator_hub
from tgbot.services.logger import LoggerFormatter, FORMAT

# Конфигурация логирования
logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(), logging.FileHandler('tgbot/log/my_log.log', 'w')]
)
logging.getLogger().handlers[0].setFormatter(LoggerFormatter())
logging.getLogger().handlers[1].setFormatter(logging.Formatter(FORMAT))

log = logging.getLogger(__name__)

# Отключить дублирование логирования SQLAlchemy
from sqlalchemy import log as sqlalchemy_log

sqlalchemy_log._add_default_handler = lambda x: None


async def main():
    log.debug('Bot init...')

    # Инициализация конфигурации бота
    config: Config = load_config()

    # Подключение к базе данных и создание репозитория
    repo = create_repo(config.db)

    # Создание таблиц
    if config.db.create_tables:
        await repo.create_tables()

    # Инициализация бота
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # Инициализация временного хранилища
    storage = MemoryStorage()

    # Инициализация диспетчера
    dp = Dispatcher(storage=storage, repo=repo)

    # Инициализация fluentogram
    translator_hub: TranslatorHub = create_translator_hub()

    # Регистрация роутеров
    dp.include_routers(  # Роутеры хэндлеров
        user_router,
    )
    dp.include_routers(  # Роутеры диалогов
        start_dialog,
        psychology_dialog,
        tests_dialog,
        profile_dialog,
    )

    # Регистрация миддлварей
    dp.update.middleware(TranslatorRunnerMiddleware())  # i18n
    # dp.update.middleware(MyMiddleware(repo))

    # Инициализация aiogram-dialog
    setup_dialogs(dp)

    # Запуск бота
    log.info('Start bot...')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == '__main__':
    asyncio.run(main())
