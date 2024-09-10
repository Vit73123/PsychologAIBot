import logging

from aiogram import Bot
from aiogram.types import BotCommand, Message

log = logging.getLogger(__name__)


# Создать основное меню и вывести кнопку Menu
async def create_main_menu(bot: Bot):
    log.debug("Create main menu")

    main_menu_commands = [
        BotCommand(command='/start',
                   description='Добро пожаловать в Бот!'),
    ]
    await set_main_menu(commands=main_menu_commands, bot=bot)


# Установить команды
async def set_main_menu(commands: list[BotCommand], bot: Bot):
    await bot.delete_my_commands()
    await bot.set_my_commands(commands)


# Удалить команды и кнопку Menu
async def del_main_menu(message: Message, bot: Bot):
    log.debug("Remove main menu")

    await bot.delete_my_commands()
    await bot.send_message(chat_id=message.chat.id, text='Кнопка "Menu" удалена', reply_markup=None)
