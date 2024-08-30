from tgbot.db.repo import DbRepo
from .session import SessionDTO
from .status import StatusDTO
from .user import UserDTO


class DbDTO:
    user: UserDTO
    session: SessionDTO
    status: StatusDTO

    repo: DbRepo

    def __init__(self, repo: DbRepo):
        self.repo = repo
        self.user = UserDTO(repo)
        self.session = SessionDTO(repo)
        self.status = StatusDTO(repo)

    async def create_tables(self):
        await self.repo.create_tables()
