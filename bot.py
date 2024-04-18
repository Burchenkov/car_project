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
class CarForm(StatesGroup): #-----------
    waiting_for_brand = State() #-----------
    waiting_for_model = State() #-----------
    waiting_for_year = State() #-----------

bot = Bot (token = API_TOKEN)
dp = Dispatcher()

list = []
"7082797338:AAGFiO9JvT20WMNyJO6xDSXBnMibz4sQGe0"


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
    await state.set_state(CarForm.waiting_for_brand)
    await message.answer('Вы добавили простую машину! Укажите марку: ')




@dp.message(CarForm.waiting_for_model)
async def model_received(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await state.set_state(CarForm.waiting_for_year)
    await message.answer("Какой год выпуска?")

@dp.message(CarForm.waiting_for_year)
async def year_received(message: types.Message, state: FSMContext):
    data = await state.get_data()
    brand = data['brand']
    model = data['model']
    year = message.text
    await message.answer(f"Спасибо! Машина {brand} {model} {year} года добавлена.")
    await state.clear()
       
async def main():
    await dp.start_polling(bot)

if __name__== '__main__':
    asyncio.run(main())
    