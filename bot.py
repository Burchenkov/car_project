import asyncio

from aiogram.fsm.state import State, StatesGroup #-----------
from aiogram.fsm.context import FSMContext #-----------
from aiogram.filters.command import CommandStart  #-----------
from aiogram.filters.state import Filter #-----------  
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command 
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from class1 import Car





API_TOKEN = '6736639037:AAGxAVGV6VBMMyRgeIDGgseYb5_VEYRY9Xc'
class Car(StatesGroup): #-----------
    waiting_for_brand = State() #-----------
    waiting_for_model = State() #-----------
    waiting_for_year = State() #-----------
    waiting_for_specialization = State() #-----------
    waiting_for_country = State() #-----------

bot = Bot (token = API_TOKEN)
dp = Dispatcher()

list = []



@dp.message(Command('start'))
async def start_adding_car(message: types.Message):
    
    kb = [
        [types.KeyboardButton(text='/simple')],
        [types.KeyboardButton(text='/special')]
        
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Какую машину хотите добавить?', reply_markup=keyboard)
    
          
@dp.message(Command('simple'))
async def send_simple(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    await state.set_state(Car.waiting_for_brand)
    await message.answer('Вы добавили простую машину! Укажите марку: ')


@dp.message(Car.waiting_for_brand)
async def brand_received(message: types.Message, state: FSMContext):
    await state.update_data(brand=message.text)
    await state.set_state(Car.waiting_for_model)
    await message.answer("Какую модель?")

@dp.message(Car.waiting_for_model)
async def model_received(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await state.set_state(Car.waiting_for_year)
    await message.answer("Какой год выпуска?")

@dp.message(Car.waiting_for_year)
async def year_received(message: types.Message, state: FSMContext):
    data = await state.get_data()
    brand = data['brand']
    model = data['model']
    year = message.text
    await message.answer(f"Спасибо! Машина {brand} {model} {year} года добавлена.")
    await state.clear()


@dp.message(Command('special'))
async def send_special(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    await state.set_state(Car.waiting_for_brand)
    await message.answer('Вы добавили специальную машину! Укажите марку: ')


@dp.message(Car.waiting_for_brand)
async def brand_special_received(message: types.Message, state: FSMContext):
    await state.update_data(brand=message.text)
    await state.set_state(Car.waiting_for_model)
    await message.answer("Какую модель?")

@dp.message(Car.waiting_for_model)
async def model_special_received(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await state.set_state(Car.waiting_for_year)
    await message.answer("Какой год выпуска?")

@dp.message(Car.waiting_for_specialization)
async def specialization_special_received(message: types.Message, state: FSMContext):
    await state.update_data(specialization=message.text)
    await state.set_state(Car.waiting_for_specialization)
    await message.answer("Какая специализация?")

@dp.message(Car.waiting_for_country)
async def country_special_received(message: types.Message, state: FSMContext):
    await state.update_data(country=message.text)
    await state.set_state(Car.waiting_for_country)
    await message.answer("Какая страна производство?")






@dp.message(Car.waiting_for_country)
async def year_received(message: types.Message, state: FSMContext):
    data = await state.get_data()
    brand = data['brand']
    model = data['model']
    year = message.text
    specialization = data['specialization'] 
    country = ['country']
    await message.answer(f"Спасибо! Машина {brand} {model} {year} года {specialization} {country} добавлена.")
    await state.clear()
       
async def main():
    await dp.start_polling(bot)

if __name__== '__main__':
    asyncio.run(main())
    