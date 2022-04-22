from aiogram import types
from loader import dp
from keyboard.inline_keyboard import inline_keyboard

@dp.message_handler(text = '1')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Ты выбрал 1')


@dp.message_handler(text='2')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Ты выбрал 2')


@dp.message_handler(text='3')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Ты выбрал 3')


@dp.message_handler(text='Текст 1')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Ты выбрал Текст 1')


@dp.message_handler(text='Текст 2')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Ты выбрал Текст 2')


@dp.message_handler(text='инлайн')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Ты выбрал инлайн меню', reply_markup=inline_keyboard)
