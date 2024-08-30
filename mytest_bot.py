import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from fluentogram import TranslatorHub

from tgbot.config.config import Config, load_config
from tgbot.dialogs import (
    mytest_start_dialog,
    mytest_1_dialog,
)
from tgbot.handlers import (
    mytest_router,
)
from tgbot.middlewares.i18n import TranslatorRunnerMiddleware
from tgbot.services.i18n import create_translator_hub
from tgbot.services.logger import LoggerFormatter, FORMAT

# Конфигурация логирования
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(), logging.FileHandler('resources/log/my_test_log.log', 'w')]
)
logging.getLogger().handlers[0].setFormatter(LoggerFormatter())
logging.getLogger().handlers[1].setFormatter(logging.Formatter(FORMAT))

log = logging.getLogger(__name__)


async def main():
    log.debug('Bot init...')

    # Инициализация конфигурации бота
    config: Config = load_config()

    # Инициализация бота
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # Инициализация временного хранилища
    storage = MemoryStorage()

    # Инициализация диспетчера
    dp = Dispatcher(storage=storage)

    # Инициализация fluentogram
    translator_hub: TranslatorHub = create_translator_hub()

    # Регистрация роутеров
    dp.include_routers(  # Роутеры хэндлеров
        mytest_router,
    )
    dp.include_routers(  # Роутеры диалогов
        mytest_start_dialog,
        mytest_1_dialog,
    )

    # Регистрация миддлварей
    dp.update.middleware(TranslatorRunnerMiddleware())  # i18n
    # dp.update.middleware(MyMiddleware(repo))

    # Инициализация aiogram-dialog
    setup_dialogs(dp)

    # Запуск бота
    log.info('Start bot...')
    await dp.start_polling(bot, _translator_hub=translator_hub)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
