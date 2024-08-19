import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from fluentogram import TranslatorHub

from tgbot.config.config import Config, load_config
from tgbot.handlers.user.user import router as user_router
from tgbot.middlewares.i18n import TranslatorRunnerMiddleware
from tgbot.services.i18n import create_translator_hub
from tgbot.services.logger import LoggerFormatter, FORMAT, get_logger_sel

# Конфигурация логирования
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(), logging.FileHandler('tgbot/log/my_log.log', 'w')]
)
logging.getLogger().handlers[0].setFormatter(LoggerFormatter())
logging.getLogger().handlers[1].setFormatter(logging.Formatter(FORMAT))

log = logging.getLogger(__name__)
log_sel = get_logger_sel(__name__, log.getEffectiveLevel())


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

    # Инициализация aiogram-dialog
    # setup_dialogs(dp)

    # Регистрация роутеров
    dp.include_router(user_router)

    # Регистрация миддлварей
    dp.update.middleware(TranslatorRunnerMiddleware())  # i18n

    # Запуск бота
    log.info('Start bot...')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == '__main__':
    asyncio.run(main())
