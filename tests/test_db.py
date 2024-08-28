from sqlalchemy.ext.asyncio import (
    AsyncEngine
)

from tgbot.db.queries import *
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

log_dev.debug("Save me God!")


async def get_user_test(session_pool: async_sessionmaker, user_id: int):
    log_dev.debug("Get user from db by user_id=%s", str(user_id))
    user = await get_user_by_user_id(session_pool, user_id)
    log_dev.info(user)
    pass


async def run_db_tests(engine: AsyncEngine, session_pool: async_sessionmaker):
    user_id = 5453594403
    await get_user_test(session_pool, user_id)

    pass
