import asyncio
import logging

from setup import dispatcher, bot, register_routers

log = logging.getLogger(__name__)


async def main():
    log.debug('Process my_main()...')

    # Инициализация роутеров
    log.debug('Register routers...')
    await register_routers(dispatcher=dispatcher)

    # Запуск бота
    log.info('Start bot...')
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
