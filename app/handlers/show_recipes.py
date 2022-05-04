from aiogram import Dispatcher, types
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, IDFilter
from app.logic.db_control import db

db = db()

async def cmd_show_recipe(message: types.Message):
    '''Показать рецепты из базы данных'''
    data = db.show_recipes()
    data_for_one_mess = ""
    row_in_mess = 15
    i = 0
    for elem in data:
        row = "{0}. {1}. ".format(elem[0],elem[1])
        row += (elem[2]*'\U00002B50')+'\n'
        data_for_one_mess+=row
        i+=1
        if i%row_in_mess==0:
            await message.answer(data_for_one_mess)
            data_for_one_mess=''
            i=0
            continue
    try:
        await message.answer(data_for_one_mess)
    except aiogram.utils.exceptions.MessageTextIsEmpty:
        pass

async def cmd_get_random_recipe(message: types.Message):
    '''Выдает случайный рецепт из базы данных'''
    count_random_recipes = 1
    data = db.show_recipes(count_random_recipes)
    data_for_one_mess = ""
    if count_random_recipes<15:
        row_in_mess = count_random_recipes
    else:
        row_in_mess = 15
    i = 0
    for elem in data:
        row = "{0}. {1}. ".format(elem[0],elem[1])
        row += (elem[2]*'\U00002B50')+'\n'
        data_for_one_mess+=row
        i+=1
        if i%row_in_mess==0:
            await message.answer(data_for_one_mess)
            data_for_one_mess=''
            i=0
            continue
    try:
        await message.answer(data_for_one_mess)
    except aiogram.utils.exceptions.MessageTextIsEmpty:
        pass


def register_handler_show_recipe(dp: Dispatcher):
    dp.register_message_handler(cmd_show_recipe, commands="showrecipes")
    dp.register_message_handler(cmd_get_random_recipe, commands="randomrecipe")