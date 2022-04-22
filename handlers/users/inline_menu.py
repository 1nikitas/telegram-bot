from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboard.inline_keyboard import inline_keyboard

@dp.message_handler(text='инлайн')
async def show_inline_menu(message: types.Message):
    await message.answer("Инлайн меню нижe", reply_markup=inline_keyboard)
print("Выбарли инлайн меню")