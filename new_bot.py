#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import json

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
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from class1 import Car, New_car, CarEncoder

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

model = None
country = None
spec = None
car_up = None
year = None
type = None
car_id = None

def save_cars_to_file(cars, file_path):
    with open(file_path, "w") as file:
        json.dump(cars, file, cls=CarEncoder, indent=4)

def load_cars_from_file(file_path):
    def car_decoder(dct):
        if 'spec' in dct:
            return New_car(**dct)
        return Car(**dct)

    try:
        with open(file_path, "r") as file:
            return {int(car_id): car_decoder(car) for car_id, car in json.load(file).items()}
    except FileNotFoundError:
        return {}

FILE_PATH = "cars.json"
cars = []

import openpyxl

def to_list(self): 
        return [self.car_id, self.year, self.country, self.brand, self.payload_capacity, self.specialization] 
class CarStorage: 
    def __init__(self, file_name): 
        self.car_list = [] 
        self.next_id = 1 
        self.file_name = file_name


def save_to_excel(self): 
    wb = openpyxl.load_workbook(self.user_cars_data.xlsx) 
    ws = wb.active 

    for car_list in self.cars: 
        ws.append(сar.to_list()) 

    wb.save(self.user_cars_data.xlsx) 
    #print(f"Данные успешно сохранены в файл {self.user_cars_data.xlsx}")

file_xlsx = CarStorage("user_cars_data.xlsx")

#------------------------------------------------------------------------
@dp.message(Command('start'))
async def start_adding_car(message: types.Message, state=FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text = 'simple'),
        types.KeyboardButton(text='special')
    )
    print(message.text)
    await message.answer("Какую машину вы хотите добавить?", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text.lower() == 'special')
async def send_special(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    global type
    type=message.text
    print(f"ТИП МАШИНЫ {type}")
    await state.set_state(CarForm.waiting_for_spec)
    await message.answer("Добавим специальную машину! Укажите спецализацию: ")
    return type

@dp.message(F.text.lower() == 'simple')
async def send_simple(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    global type
    type=message.text
    print(f"ТИП МАШИНЫ {type}")
    await state.set_state(CarForm.waiting_for_model)
    await message.answer("Добавим простую машину! Укажите марку: ")

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
    global a
    if type == "simple":
        data = await state.get_data()
        model = data['model']
        country = data['country']
        year = message.text
        main_car = Car(year, country, model)
    elif type == "special":
        data = await state.get_data()
        model = data['model']
        country = data['country']
        year = message.text
        main_car = New_car(year, country, model, car_up, spec)

    cars.append(main_car)
    save_cars_to_file(cars, FILE_PATH)

    await message.answer("Машина записана в файл")
    await state.clear()
        
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text = 'simple'),
        types.KeyboardButton(text='special'),
        types.KeyboardButton(text='exel'),
        )
    await message.answer(
        "Хотите добавить еще простую или специальную машину? Или выгрузить в EXEL?", 
        reply_markup=builder.as_markup(resize_keyboard=True)
        )


@dp.message(F.text.lower() == 'exel')
async def send_special(message: types.Message, state=FSMContext):
    
    car_list = load_cars_from_file(FILE_PATH)
    print(cars)
    save_to_excel()

    await message.answer("Выгружаю в Exel, но это не точно...")



#------------------------------------------------------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())