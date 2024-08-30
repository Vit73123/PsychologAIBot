from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from tgbot.utils.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class SessionRepo:
    pool: async_sessionmaker[AsyncSession]

    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool
