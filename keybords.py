from aiogram.types import ReplyKeyboardMarkup,KeyboardButton




kb=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Регистрация')],
                                 [KeyboardButton(text='Проверить'),
                                  KeyboardButton(text='Информация')]], resize_keyboard=True,)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Назад', callback_data='back'))
