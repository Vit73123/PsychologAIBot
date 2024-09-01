import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from tgbot.config import Config, load_config
from tgbot.db.factory import (create_engine,
                              create_repo,
                              create_tables, )
from tgbot.dialogs import (start_dialog,
                           psychology_dialog,
                           tests_dialog,
                           profile_dialog, )
from tgbot.filters import IsAdmin
from tgbot.handlers import user_router
from tgbot.middlewares.i18n import TranslatorRunnerMiddleware
from tgbot.tools.i18n import create_translator_hub
from tgbot.tools.logger import LoggerFormatter, FORMAT

# Конфигурация логирования
logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(), logging.FileHandler('resources/log/bot.log', 'w')]
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

    # Подключение к базе данных
    engine = create_engine(config.db)
    repo = create_repo(engine)

    # Создание таблиц
    if config.db.create_tables:
        await create_tables(engine, config.db)

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

    # Фильтр IsAdmin
    IsAdmin.admin_ids = config.tg_bot.admin_ids

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
