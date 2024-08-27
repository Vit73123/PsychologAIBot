import asyncio

from tests.test_db import run_db_tests
from tgbot.config.config import Config, load_config
from tgbot.db.engine import create_pool


async def main():
    config: Config = load_config()

    session_pool = create_pool(config.db)

    await run_db_tests(session_pool)


if __name__ == '__main__':
    asyncio.run(main())
