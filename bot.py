from unittest import skip
from aiogram import Bot, Dispatcher, executor, types
import logging
from func.defs import *
from func.token import token
from func.database import database

#Создали бота
bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

#Создали базу данных
db = database()
db.init()

#Логика бота
@dp.message_handler(commands="start")
async def b_start(message: types.Message):
    await start(message)


if __name__== "__main__":
    executor.start_polling(dp, skip_updates=True)