from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, IDFilter
from app.logic.db_control import db


async def cmd_start(message: types.Message, state: FSMContext):
    '''Первое сообщение'''
    await state.finish()
    await message.answer("Добро пожаловать в мою таверну!")



def register_handler_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")

