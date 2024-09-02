from tgbot.db.dao import StatusDAO
from tgbot.db.models import Status


def create_status_to_dao(status: Status):
    return StatusDAO(
        status_id=status.id,
        text=status.text,
        grade=status.grade
    )


def create_status_from_dao(status_dao: StatusDAO):
    status = Status()
    status.id = status_dao.id
    status.text = status_dao.text
    status.grade = status_dao.grade
    return status
