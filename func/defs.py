from aiogram import types

def hello(message: types.Message):
    return message.answer("Проверочка на вшивость")