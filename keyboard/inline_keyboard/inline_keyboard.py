from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text='Сообщение', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Ссылка", callback_data="Где-то тут ссылка)")
                                            ],
                                           [InlineKeyboardButton(text='Сообщение', callback_data='Сообщение'),
                                            InlineKeyboardButton(text="Ссылка", callback_data="Где-то тут ссылка)")
                                            ]
                                       ]
                                       )