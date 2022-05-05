import re
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext


async def cmd_start(message: types.Message, state: FSMContext):
    '''Первое сообщение'''
    await state.finish()
    await message.answer("Hello!")


def register_handler_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")

if __name__ == "__main__":

    pass