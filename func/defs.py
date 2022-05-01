from aiogram import types

def start(message: types.Message):
    return message.answer("Добро пожаловать в мою таверну!")

