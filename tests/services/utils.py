from aiogram import Bot


async def on_startup(bot: Bot):
    await bot.send_message(chat_id=5453594403, text='/start')

