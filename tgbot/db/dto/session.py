from tgbot.db.repo.session import SessionRepo


class SessionDTO:
    _repo: SessionRepo

    def __init__(self, repo: SessionRepo):
        self._repo = repo
