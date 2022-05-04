from aiogram import Dispatcher, types
import aiogram
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text, IDFilter
from app.logic.db_control import db
import re

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
    data = db.show_recipes(count_random_recipes, rnd_choice=True)
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

async def choice_recipe(message:types.Message):
    '''Показыавет выбранный рецепт'''
    data = db.show_recipes(int(message.text), rnd_choice=False)
    if len(data) != 0:
        data_for_one_mess = ""
        for elem in data:
            data_for_one_mess = "{0}. {1}. ".format(elem[0],elem[1])
            data_for_one_mess += (elem[2]*'\U00002B50')+'\n'
            data_for_one_mess += elem[3]
            await message.answer(data_for_one_mess)
    else:
            await message.answer("Такого номера в базе нет")


def register_handler_show_recipe(dp: Dispatcher):
    dp.register_message_handler(cmd_show_recipe, commands="showrecipes")
    dp.register_message_handler(cmd_get_random_recipe, commands="randomrecipe")
    dp.register_message_handler(choice_recipe, filters.Regexp(r'[^\d]+'))