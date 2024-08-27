from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    dsn: str  # Подключение к базе данных по DSN
    is_echo: bool  # Вывод лога СУБД


@dataclass
class GPT:
    token: str  # Токен для доступа к GPT
    url: str  # URL-адрес для запросов к GPT


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    gpt: GPT
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        gpt=GPT(
            token=env('GPT_TOKEN'),
            url=env('GPT_URL')
        ),
        db=DatabaseConfig(
            dsn=env('DB_DSN'),
            is_echo=True if env('DB_IS_ECHO') == 'yes' else False
        )
    )
