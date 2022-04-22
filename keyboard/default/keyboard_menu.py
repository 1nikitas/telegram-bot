from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2')
        ],
        [
            KeyboardButton(text='3')
        ],
        [
            KeyboardButton(text='Текст 1'),
            KeyboardButton(text='Текст 2)'),
            KeyboardButton(text='инлайн')
        ]
    ], resize_keyboard=True
)