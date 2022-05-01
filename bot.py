from email import message
import imp
import sqlite3 as sq
from unittest import skip
from aiogram import Bot, Dispatcher, executor, types
import logging
from func.defs import *
from func.token import token

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


if __name__== "__main__":
    executor.start_polling(dp, skip_updates=True)