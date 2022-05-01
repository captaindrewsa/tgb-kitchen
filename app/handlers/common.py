from atexit import register
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, IDFilter

async def cmd_start(message: types.Message):
    '''Первое сообщение'''
    await message.answer("Добро пожаловать в мою таверну!")



def register_handler_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")