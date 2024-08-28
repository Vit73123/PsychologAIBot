from logging import getLogger

from sqlalchemy.ext.asyncio import async_sessionmaker

from tgbot.db.repo import Repo
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

log_dev.debug("Save me God!")


async def get_user_test(session: async_sessionmaker, repo: Repo, user_id: int):
    log_dev.info(" Get user id=%s", user_id)

    user = await repo.user.get_user_by_user_id(session, user_id)
    log_dev.info(" user: %s", user)

    pass

async def run_db_tests(session: async_sessionmaker, repo: Repo):

    user_id = 5453594403
    await get_user_test(session, repo, user_id)

    pass
