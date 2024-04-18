#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio

import pickle

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
    waiting_for_spec = State() #-----------

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# model = None
# country = None
# spec = None
# car_up = None
# year = None
type = None

#------------------------------------------------------------------------
@dp.message(Command('start'))
async def start_adding_car(message: types.Message):
    await message.answer("Какую машину вы хотите добавить? simple/special")

@dp.message(Command('simple'))
async def send_simple(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    type=message.text
    print(f"ТИП МАШИНЫ {type}")
    await state.set_state(CarForm.waiting_for_model)
    await message.answer("Добавим простую машину! Укажите марку: ")
    #return type

@dp.message(Command('special'))
async def send_special(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    type=message.text
    await state.set_state(CarForm.waiting_for_spec)
    await message.answer("Добавим специальную машину! Укажите спецализацию: ")
    #return type

@dp.message(CarForm.waiting_for_spec)
async def spec_received(message: types.Message, state: FSMContext):
    await state.update_data(spec=message.text)
    await state.set_state(CarForm.waiting_for_car_up)
    await message.answer("Какая высота машины?")

@dp.message(CarForm.waiting_for_car_up)
async def car_up_received(message: types.Message, state: FSMContext):
    await state.update_data(car_up=message.text)
    await state.set_state(CarForm.waiting_for_model)
    await message.answer("Какая модель?")

@dp.message(CarForm.waiting_for_model)
async def model_received(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await state.set_state(CarForm.waiting_for_country)
    await message.answer("Какая страна?")

@dp.message(CarForm.waiting_for_country)
async def country_received(message: types.Message, state: FSMContext):
    await state.update_data(country=message.text)
    await state.set_state(CarForm.waiting_for_year)
    await message.answer("Какой год выпуска?")

@dp.message(CarForm.waiting_for_year)
async def year_received(message: types.Message, state: FSMContext):
    data = await state.get_data()
    model = data['model']
    country = data['country']
    spec = data['spec']
    car_up = data['car_up']
    year = message.text

    print(f"Тип машины текушший {type}")
    
    a=(Car(year, country, model))
    
    with open("table.txt", "wb") as t:
        
        pickle.dump(a, t)

    await message.answer(f"Спасибо! Машина {country} {model} {year} года добавлена. Напищите simple/special чтобы добавить еще!")
    await state.clear()
#------------------------------------------------------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())