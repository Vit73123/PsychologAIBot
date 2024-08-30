from aiogram import Bot


async def on_startup(bot: Bot):
    await bot.send_message(text='/start')
