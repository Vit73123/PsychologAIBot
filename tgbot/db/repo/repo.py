from sqlalchemy.ext.asyncio import (
    async_sessionmaker
)

from .appointment_repo import AppointmentRepo
from .status_repo import StatusRepo
from .user_repo import UserRepo


class Repo:

    def __init__(self, pool: async_sessionmaker):
        self.pool = pool

        self.user = UserRepo(self.pool)
        self.appointment = AppointmentRepo(self.pool)
        self.status = StatusRepo(self.pool)
