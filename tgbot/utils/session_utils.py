from tgbot.db.dao import SessionDAO
from tgbot.db.models import Session


def create_session_to_dao(session: Session):
    return SessionDAO(
        session_id=session.id,
        review=session.review
    )


def create_status_from_dao(session_dao: SessionDAO):
    session = Session()
    session.id = session_dao.id
    session.review = session_dao.review
    return session
