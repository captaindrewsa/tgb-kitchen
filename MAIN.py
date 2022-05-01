import sqlite3 as sq
from unittest import skip
from aiogram import Bot, Dispatcher, executor, types
import logging

bot = Bot(token='5371492482:AAHPyA2Ag-X9G-6h9qtE0TXolf7NCGtMcV4')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")



if __name__== "__main__":
    executor.start_polling(dp, skip_updates=True)