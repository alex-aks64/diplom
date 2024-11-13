from mailbox import Message
from aiogram import Bot, Dispatcher, executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import threading
import time
import asyncio
import texts
from keybords import *
from registr import *




api="7703728043:AAGjr1S5qUA3m45S2XJBwKQgmcsHRvPQrrQ"
bot=Bot(token=api)
dp=Dispatcher(bot,storage= MemoryStorage())

class  RegistrationState(StatesGroup):
    username = State()
    firstname = State()
    phone = State()


@dp.message_handler(text=['Информация','/info'])
async def info(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Проверить'), types.KeyboardButton(text='Информация'))
    with open('photo/DwA.jpg', "rb") as dw:
        await message.answer_photo(dw,'Информация о боте:')
        time.sleep(1)
        await message.answer('Команда /start - начало работы с ботом')
        await message.answer('Команда /info - получение информации о боте',reply_markup=keyboard)


@dp.message_handler(text=['/start','/старт'])
async def task1(message):
    with open('photo/30instrum.jpg', "rb") as instrum:
        await message.answer_photo(instrum,f"Привет: {message.from_user.username}" ,reply_markup=kb)
    time.sleep(1)
    await message.answer(f"Этот бот помогает отследить вам что вы брали со склада.")
    time.sleep(1)
    await  message.answer(f"Какие  инструменты вы должны принести и сдать ")
thread1 = threading.Thread(target=task1)
thread1.start()
thread1.join()

# Проверка осуществляется по номеру телефона
class  CheckPhone(StatesGroup):
    phone = State()
@dp.message_handler(text=['Проверить'])
async def start(message: types.Message):
    await message.reply(texts.ts_m)
    await CheckPhone.phone.set()


@dp.message_handler(state=CheckPhone.phone)
async def check_phone_number(message: types.Message, state: FSMContext):
    phone = message.text.strip()
    product_data = get_phon_data(phone)
    user_data = get_user_data(phone)
    print(product_data, user_data, type(product_data), type(user_data))
    if product_data:
        if user_data[2] == product_data[3]:
            user_info = format_user_data(user_data)
            product_info = format_product_data(product_data)
            with open('photo/Hh.jpg', "rb") as hh:
                await message.answer_photo(hh,f"{user_info}\n{product_info}")
        else:
            await message.reply('Телефон не найден')
            await state.finish()



def format_user_data(user_data):
    user_info = f"Имя: {user_data[0]}\n"
    user_info += f"Фамилия: {user_data[1]}\n"
    user_info += f"Телефон: {user_data[2]}\n"
    return user_info


def format_product_data(product_data):
    product_info = f"Название: {product_data[1]}\n"
    product_info += f"Описание: {product_data[2]}\n"
    product_info += f"Телефон: {product_data[3]}\n"
    return product_info
  
# -----------------------------------



# Регистрация стек
@dp.message_handler(text='Регистрация')
async def sing_up(message: types.Message):
    with open('photo/wtN.jpg', "rb") as wt:
        await message.answer_photo(wt,"Введите имя пользователя (только латинский алфавит):")
        await RegistrationState.username.set()


@dp.message_handler(state = RegistrationState.username)
async def set_username(message,state):
        if is_included(message.text):
            await message.answer("Пользователь существует, введите другое имя")
            await RegistrationState.username.set()
        else:
            await state.update_data(username=message.text)
            await message.answer("Введите свою Фамилию:")
            await RegistrationState.firstname.set()


@dp.message_handler(state= RegistrationState.firstname)
async def set_email(message,state):
    await state.update_data(firstname=message.text)
    await message.answer("Введите свой номер телефона Пример: 932-445-43-09")
    await RegistrationState.phone.set()


@dp.message_handler(state= RegistrationState.phone)
async def set_age(message, state):
    await state.update_data(phone=message.text)
    users_data= await state.get_data()
    try:
        add_user(username=users_data["username"],firstname=users_data["firstname"],phone=int(users_data["phone"],))
        await state.finish()
        with open('photo/b9.jpeg', "rb") as b:
            await message.answer_photo(b,f'Увожаемый пользователь {message.from_user.username}\n Регистрация прошла успешна.')
    except ValueError:
        await message.answer(f'Увожаемый пользователь {message.from_user.username}\n нажмите назад для повторной реги')
        await state.finish()
# добавления инструментов
class  Registration(StatesGroup):
    title = State()
    description = State()
    phone = State()
# Админ понель
@dp.message_handler(text='/admin12')
async def sing_up(message: types.Message):
    await message.answer("Введите название товара:")
    await Registration.title.set()


@dp.message_handler(state = Registration.title)
async def set_username(message,state):
    await state.update_data(title=message.text)
    await message.answer("ведите описание  товара")
    await Registration.description.set()



@dp.message_handler(state= Registration.description)
async def set_email(message,state):
    await state.update_data(description=message.text)
    await message.answer("Введите свой номер телефона:")
    await Registration.phone.set()


@dp.message_handler(state= Registration.phone)
async def set_age(message, state):
    await state.update_data(phone=message.text)
    product_data= await state.get_data()
    try:
        add_product(title=product_data["title"],description=product_data["description"],phone=int(product_data["phone"],))
        await state.finish()
        with open('photo/b9.jpeg', "rb") as b:
            await message.answer_photo(b,f'Увожаемый пользователь {message.from_user.username}\n Регистрация прошла успешна.')
    except ValueError:
        await message.answer(f'Увожаемый пользователь {message.from_user.username}\n нажмите назад для повторной реги')
        await state.finish()




# повторщик
@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"Привет: {message.from_user.first_name}")
    time.sleep(1)
    await message.answer("Этот бот помогает отследить вам что вы брали со склада. ")


if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)