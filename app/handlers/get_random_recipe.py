from os import sync
from aiogram import Dispatcher, types
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, IDFilter
from app.logic.db_control import db

db = db()

async def cmd_get_random_recipe(message: types.Message):
    '''Выдает случайный рецепт из базы данных'''
    
    pass


def register_handler_show_recipe(dp: Dispatcher):
    dp.register_message_handler(cmd_get_random_recipe, commands="randomrecipe")