from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, IDFilter
from app.logic.db_control import db

db = db()

class AddNewRecipe(StatesGroup):
    waiting_for_recipe_name = State()
    waiting_for_recipe_level = State()
    waiting_for_recipe_text = State()


async def cmd_start(message: types.Message, state: FSMContext):
    '''Первое сообщение'''
    await state.finish()
    await message.answer("Добро пожаловать в мою таверну!")



def register_handler_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")

