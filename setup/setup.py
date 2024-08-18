import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config.config import Config, load_config
from utils.logger import LoggerFormatter, FORMAT, get_logger_new

# Конфигурация логирования
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(), logging.FileHandler('log/my_log.log', 'w')]
)
logging.getLogger().handlers[0].setFormatter(LoggerFormatter())
logging.getLogger().handlers[1].setFormatter(logging.Formatter(FORMAT))

log = logging.getLogger(__name__)
log_new = get_logger_new(__name__, log.getEffectiveLevel())

log.info('Process setup()...')

# Инициализация конфигурации бота
log.debug('Init config...')
config: Config = load_config()

# Инициализация объекта хранилища
log.debug('Init storage...')
storage = MemoryStorage()

# Инициализация бота
log.debug('Init bot...')
bot = Bot(
    token=config.tg_bot.token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

# Инициализация диспетчера
log.debug('Init dispatcher...')
dispatcher = Dispatcher(storage=storage)
