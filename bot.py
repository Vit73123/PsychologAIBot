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
                           aboutme_dialog, )
from tgbot.handlers import user_router, admin_router
from tgbot.middlewares.i18n import TranslatorRunnerMiddleware
from tgbot.services.gpt import ChatGptService
from tgbot.tools.emoji import load_emoji_grades
from tgbot.tools.i18n import create_translator_hub
from tgbot.tools.json import load_json
from tgbot.tools.logger import LoggerFormatter, FORMAT, get_logger_dev
from tgbot.tools.main_menu import create_main_menu

# Конфигурация логирования
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(), logging.FileHandler('resources/log/bot.log', 'w')]
)
logging.getLogger().handlers[0].setFormatter(LoggerFormatter())
logging.getLogger().handlers[1].setFormatter(logging.Formatter(FORMAT))

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

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

    # Эмодзи шкалы настроения
    grades: dict = load_emoji_grades(config.root_path / 'resources' / 'emoji')

    # ChatGPT
    # config.gpt.prompts_info = load_json(config.root_path / 'tgbot' / 'config' / 'prompts_info.json')

    # gpt = ChatGptService(token=config.gpt.token, url=config.gpt.url)

    # Главное меню
    await create_main_menu(bot=bot)

    # Инициализация диспетчера
    dp = Dispatcher(
        storage=storage,
        grades=grades,
        engine=engine,
        repo=repo,
        # gpt=gpt,
        config=config,
    )

    # Инициализация fluentogram
    translator_hub: TranslatorHub = create_translator_hub()

    # Регистрация роутеров
    dp.include_routers(  # Роутеры хэндлеров
        admin_router,
        user_router,
    )
    dp.include_routers(  # Роутеры диалогов
        start_dialog,
        psychology_dialog,
        tests_dialog,
        aboutme_dialog,
    )

    # Регистрация миддлварей
    dp.update.middleware(TranslatorRunnerMiddleware())  # i18n

    # Инициализация aiogram-dialog
    setup_dialogs(dp)

    # Запуск бота
    log.info('Start bot...')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == '__main__':
    asyncio.run(main())
