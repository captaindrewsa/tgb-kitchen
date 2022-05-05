from email import message
from os import sync
from aiogram import Dispatcher, types
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, IDFilter
from app.logic.db_control import db

db = db()

async def cmd_edit_recipe(message: types.Message):
    '''Выбирает и редактирует рецепт'''
    
    pass


def register_handler_editing_recipe(dp: Dispatcher):
    dp.register_message_handler(cmd_edit_recipe, aiogram.dispatcher.filters.IsReplyFilter)


if __name__ == "__main__":

    pass