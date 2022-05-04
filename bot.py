import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config import load_config
from app.handlers.common import register_handler_common
from app.handlers.add_recipe import register_handler_add_recipe
from app.handlers.show_recipes import register_handler_show_recipe

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Старт"),
        BotCommand(command="/addrecipe", description="Добавить новый рецепт"),
        BotCommand(command="/showrecipes", description="Показать все рецепты"),
        BotCommand(command="/randomrecipe", description="Получить случайный рецепт")
    ]
    await bot.set_my_commands(commands)

async def main():
    # Настройка логирования в stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    
    # Парсинг файла конфигурации
    config = load_config("config/bot.ini")

    # Объявление и инициализация объектов бота, диспетчера и бд
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрация хэндлеров
    register_handler_common(dp)
    register_handler_add_recipe(dp)
    register_handler_show_recipe(dp)
    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())