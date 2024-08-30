from tgbot.db.repo import DbRepo
from .session import SessionDTO
from .status import StatusDTO
from .user import UserDTO


class DbDTO:
    user: UserDTO
    session: SessionDTO
    status: StatusDTO

    _repo: DbRepo

    def __init__(self, repo: DbRepo):
        self._repo = repo
        self.user = UserDTO(repo.user_repo)
        self.session = SessionDTO(repo.session_repo)
        self.status = StatusDTO(repo.status_repo)

    async def create_tables(self):
        await self._repo.create_tables()
