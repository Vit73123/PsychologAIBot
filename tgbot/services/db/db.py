from tgbot.db.repo import DbRepo
from .session import SessionService
from .status import StatusService
from .user import UserService


class DbService:
    user: UserService
    session: SessionService
    status: StatusService

    _repo: DbRepo

    def __init__(self, repo: DbRepo):
        self._repo = repo
        self.user = UserService(repo.user_repo)
        self.session = SessionService(repo.session_repo)
        self.status = StatusService(repo.status_repo)

    async def create_tables(self):
        await self._repo.create_tables()
