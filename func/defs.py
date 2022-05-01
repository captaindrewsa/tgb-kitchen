from aiogram import types

async def hello(message: types.Message):
    await message.answer("Проверочка на вшивость")