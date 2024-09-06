import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from tests.dialogs import (start_dialog,
                           dialog_1_dialog)
from tests.handlers import (start_test_router,
                            user_test_router,
                            status_test_router,
                            session_test_router,
                            any_test_router, )
from tgbot.config import (Config,
                          load_config)
from tgbot.db.factory import (create_engine,
                              create_repo)
from tgbot.filters import IsAdmin
from tgbot.middlewares.i18n import TranslatorRunnerMiddleware
from tgbot.services.gpt import ChatGptService
from tgbot.tools.emoji import load_emoji_grades
from tgbot.tools.i18n import create_translator_hub
from tgbot.tools.json import load_json
from tgbot.tools.logger import (LoggerFormatter,
                                FORMAT)

# Конфигурация логирования
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(), logging.FileHandler('resources/log/test_bot.log', 'w')]
)
logging.getLogger().handlers[0].setFormatter(LoggerFormatter())
logging.getLogger().handlers[1].setFormatter(logging.Formatter(FORMAT))

log = logging.getLogger(__name__)

# Отключить дублирование логирования SQLAlchemy
from sqlalchemy import log as sqlalchemy_log

sqlalchemy_log._add_default_handler = lambda x: None


async def main():
    log.info('Bot init...')

    # Инициализация конфигурации бота
    config: Config = load_config()

    # Подключение к базе данных и создание репозитория
    engine = create_engine(config.db)
    repo = create_repo(engine)

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
    prompts_info = load_json(config.root_path / 'tgbot' / 'config' / 'prompts_info.json')
    config.gpt.prompts_info = prompts_info

    gpt = ChatGptService(token=config.gpt.token, url=config.gpt.url)

    # Инициализация диспетчера
    dp = Dispatcher(
        storage=storage,
        grades=grades,
        repo=repo,
        gpt=gpt,
        config=config,
    )

    # Инициализация fluentogram
    translator_hub: TranslatorHub = create_translator_hub()

    # Регистрация роутеров
    dp.include_routers(  # Роутеры хэндлеров
        start_test_router,
        user_test_router,
        status_test_router,
        session_test_router,
        any_test_router,
    )
    dp.include_routers(  # Роутеры диалогов
        start_dialog,
        dialog_1_dialog,
    )

    # Регистрация миддлварей
    dp.update.middleware(TranslatorRunnerMiddleware())  # i18n
    # dp.update.middleware(MyMiddleware(repo))

    # Фильтр IsAdmin()
    IsAdmin.admin_ids = config.tg_bot.admin_ids

    # Инициализация aiogram-dialog
    setup_dialogs(dp)

    # from tests.tools.tools import on_startup
    # dp.startup.register(await on_startup(bot))

    # Запуск бота
    log.info('Start bot...')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == '__main__':
    asyncio.run(main())
