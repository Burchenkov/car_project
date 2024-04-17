#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio

from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup #-----------
from aiogram.fsm.context import FSMContext #-----------
from aiogram.filters.command import CommandStart  #----------- 
from aiogram.filters.command import CommandStart  #-----------
from aiogram.filters.state import Filter #-----------  
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command 
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from class1 import Car

API_TOKEN = '6773453600:AAGmMXq-MGKleUj0QX7_T65cu_PS4lfHAJc'
# API_TOKEN = '6519487700:AAFsMPqa-LhsW2NVxxsRlOvvogBvhgPD4HY'


class CarForm(StatesGroup): #-----------
    waiting_for_model = State() #-----------
    waiting_for_country = State() #-----------
    waiting_for_year = State() #-----------
    waiting_for_car_up = State() #-----------
    waiting_for_specialization = State() #-----------

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

list = []

#------------------------------------------------------------------------
@dp.message(Command('start'))
async def start_adding_car(message: types.Message):
    await message.answer("Какую машину вы хотите добавить? simple/special")

@dp.message(Command('simple'))
async def send_simple(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    await state.set_state(CarForm.waiting_for_brand)
    await message.answer("Вы добавили простую машину! Укажите марку: ")

@dp.message(CarForm.waiting_for_brand)
async def brand_received(message: types.Message, state: FSMContext):
    await state.update_data(brand=message.text)
    await state.set_state(CarForm.waiting_for_model)
    await message.answer("Какую модель?")

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

    a=(Car(year, country, model))
    
    with open("table.txt", "wb") as t:
        
        pickle.dump(a, t)

    await message.answer(f"Спасибо! Машина {country} {model} {year} года добавлена.")
    await state.clear()
#------------------------------------------------------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())