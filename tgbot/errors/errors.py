from logging import getLogger

log = getLogger(__name__)


class UserIdError(Exception):

    def __init__(self, source):
        self.source = source

    def __str__(self):
        log.critical(" %s: User id is invalid or does not have permissions!", self.source)
        return f" {self.source}: User is invalid or does not have permissions!"

class UserNotRegisteredError(Exception):

    def __init__(self, source):
        self.source = source

    def __str__(self):
        log.critical(" %s User is not registered!", self.source)
        return f" {self.source}: User is not registered!"
