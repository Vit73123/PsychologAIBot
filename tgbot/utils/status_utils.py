from logging import getLogger
from typing import TYPE_CHECKING

from tgbot.db.dao import StatusDAO
from tgbot.db.models import Status
from tgbot.tools.logger import get_logger_dev

if TYPE_CHECKING:
    pass

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def create_status_to_dao(status: Status) -> StatusDAO | None:
    if status:
        return StatusDAO(
            status_id=status.id,
            text=status.text,
            grade=status.grade,
            user_id=status.user_id
        )


def create_status_from_dao(status_dao: StatusDAO) -> Status | None:
    if status_dao:
        status = Status()
        status.id = status_dao.id
        status.text = status_dao.text
        status.grade = status_dao.grade
        status.user_id = status_dao.user_id
        return status

