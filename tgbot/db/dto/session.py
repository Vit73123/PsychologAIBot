from tgbot.db.repo import DbRepo


class SessionDTO:
    _repo: DbRepo

    def __init__(self, repo: DbRepo):
        self._repo = repo
