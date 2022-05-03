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

async def cmd_add_recipe_start(message: types.Message):
    '''Инициация записи названия рецепта. 0'''
    await message.answer("Вы захотели добавить рецепт! Если вы захотите отменить запись - наберите 'отмена' ")
    await message.answer("Введите название блюда: ")
    await AddNewRecipe.waiting_for_recipe_name.set()

async def recipe_name_chosen(message: types.Message, state: FSMContext):
    '''Запись уровня рецепта. 1'''
    if message.text.lower() == "отмена":
        await state.finish()
        await message.answer("Вы прекратили добавление рецепта")
    else:
        await state.update_data(recipe_name = message.text)
        await message.answer("Теперь введите сложность блюда от 0 до 5: ")
        await AddNewRecipe.waiting_for_recipe_level.set()

async def recipe_level_chosen(message: types.Message, state: FSMContext):
    '''Запись текста рецепта. 2'''
    if message.text.lower() == "отмена":
        await state.finish()
        await message.answer("Вы прекратили добавление рецепта")
    else:
        await state.update_data(recipe_level = int(message.text))
        await message.answer("Теперь введите краткий рецепт: ")
        await AddNewRecipe.waiting_for_recipe_text.set()

async def recipe_text_chosen(message: types.Message, state: FSMContext):
    '''Завершение записи рецепта 3'''
    if message.text.lower() == "отмена":
        await state.finish()
        await message.answer("Вы прекратили добавление рецепта")
    else:
        await state.update_data(recipe_text = message.text)
        await message.answer("Рецепт добавлен!")
        user_data = await state.get_data()
        await message.answer(f"Вы добавили:\nНазвание: {user_data['recipe_name']}\nСложность: {user_data['recipe_level']}\nРецепт:\n{user_data['recipe_text']}")
        await state.finish()
        db.add_recipe(user_data)

def register_handler_add_recipe(dp: Dispatcher):
    dp.register_message_handler(cmd_add_recipe_start, commands="addrecipe", state="*")
    dp.register_message_handler(recipe_name_chosen, state=AddNewRecipe.waiting_for_recipe_name)
    dp.register_message_handler(recipe_level_chosen, state=AddNewRecipe.waiting_for_recipe_level)
    dp.register_message_handler(recipe_text_chosen, state=AddNewRecipe.waiting_for_recipe_text)