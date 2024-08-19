import logging
from logging import Logger

from tgbot.services.colors import Colors as c

FORMAT = ("#%(levelname)-8s "
          "[%(asctime)s] "
          "%(filename)-14s:%(lineno)-3d: "
          "%(message)s")


class LoggerFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: c.FOREGROUND_DARK_GREEN.value + FORMAT + c.RESET.value,
        logging.INFO: c.FOREGROUND_DARK_YELLOW.value + FORMAT + c.RESET.value,
        logging.WARNING: c.FOREGROUND_DARK_BLUE.value + FORMAT + c.RESET.value,
        logging.ERROR: c.FOREGROUND_DARK_RED.value + FORMAT + c.RESET.value,
        logging.CRITICAL: c.BACKGROUND_BLACK.value + c.FOREGROUND_RED.value + FORMAT + c.RESET.value,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class LoggerFormatterSelected(logging.Formatter):
    FORMATS = {
        logging.DEBUG: c.FOREGROUND_GREEN.value + FORMAT + c.RESET.value,
        logging.INFO: c.FOREGROUND_YELLOW.value + FORMAT + c.RESET.value,
        logging.WARNING: c.FOREGROUND_BLUE.value + FORMAT + c.RESET.value,
        logging.ERROR: c.FOREGROUND_DARK_RED.value + FORMAT + c.RESET.value,
        logging.CRITICAL: c.BACKGROUND_BLACK.value + c.FOREGROUND_RED.value + FORMAT + c.RESET.value,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger_dev(name: str, level: int) -> Logger:
    name = name + "dev"
    log = logging.getLogger(name)
    log.setLevel(level)
    log.propagate = False

    handler = logging.StreamHandler()
    handler.setLevel(level)

    handler.setFormatter(LoggerFormatterSelected())

    log.addHandler(handler)

    return log
