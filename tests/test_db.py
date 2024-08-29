from logging import getLogger

from tgbot.db import Repo
from tgbot.services.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

log_dev.debug("Save me God!")


async def get_user_test(repo: Repo, user_id: int):
    log_dev.info(" Get user: id=%s", user_id)

    user = await repo.user.get_user(user_id)
    log_dev.info(" user: %s", user)


async def run_db_tests(repo: Repo):
    user_id = 5453594404

    await get_user_test(repo, user_id)