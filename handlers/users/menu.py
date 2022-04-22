from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboard.default import keyboard_menu
@dp.message_handler(Command('menu'))
async def menu(message: types.Message):
    await message.answer("Выберите цифру из меню ниже", reply_markup=keyboard_menu)