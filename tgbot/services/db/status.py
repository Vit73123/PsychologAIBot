from tgbot.db.repo.status import StatusRepo


class StatusService:
    _repo: StatusRepo

    def __init__(self, repo: StatusRepo):
        self._repo = repo
