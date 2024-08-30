from tgbot.db.repo.session import SessionRepo


class SessionService:
    _repo: SessionRepo

    def __init__(self, repo: SessionRepo):
        self._repo = repo
