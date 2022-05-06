from aiogram import Dispatcher, types
from app.logic.db_control import db
import re


db = db()

# class EditigRecipe(StatesGroup):
#     waiting_for_name = State()
#     waiting_for_level = State()
#     waiting_for_recipe = State()

# async def start_edit_recipe(message: types.Message, state = FSMContext):
#     '''Запускает редактирование рецепта'''
#     if message.reply_to_message:
#         await state.finish()
#         await message.answer("Вы решили обновить рецепт! Еслли захотите остановить замену - наберите \"отмена\"")
#         await message.answer("Введите новое название блюда:")
#         await state.update_data(reply_message = message.reply_to_message.text)
#         await EditigRecipe.waiting_for_name.set()

# async def add_new_name_recype(message: types.Message, state = FSMContext):
#     if message.text.lower() == 'отмена':
#         await message.answer("Вы прекратили редактирование рецепта")
#         await message.answer((await state.get_data())['reply_message'])
#         # data = db.show_recipes(id_recype, rnd_choice=False)
#         # data_for_one_mess = ""
#         # for elem in data:
#         #     data_for_one_mess = "{0}. {1}. ".format(elem[0],elem[1])
#         #     data_for_one_mess += (elem[2]*'\U00002B50')+'\n'
#         #     data_for_one_mess += elem[3]
#         #     await message.answer(data_for_one_mess)
#     else:
#         await state.update_data(new_name = message.text)
#         await message.answer("Теперь введите сложность блюда от 1 до 5: ")
#         await EditigRecipe.waiting_for_level.set()

# async def add_new_level_recype(message: types.Message, state = FSMContext):
#     if message.text.lower() == 'отмена':
#         await message.answer("Вы прекратили редактирование рецепта")
#         await message.answer((await state.get_data())['reply_message'])

async def edit_recipe(message: types.Message):
    if message.reply_to_message and re.match(re.compile('[0-9]'),message.reply_to_message.text):
        list_data = message.text.split(": ")
        if list_data[0].lower() == 'сложность' and 0>int(list_data[1])>5:
            await message.answer("Значение сложности должно быть в диапазоне от 0 до 5")
        else:
            list_data.append(re.findall(re.compile('[0-9]'), message.reply_to_message.text)[0])

            db.edit_recipe(list_data[1], list_data[2] , list_data[0])
            await message.answer("Данные изменены!")




def register_handler_editing_recipe(dp: Dispatcher):
    dp.register_message_handler(edit_recipe)

if __name__ == "__main__":

    pass