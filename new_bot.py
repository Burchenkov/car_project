#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import json
import openpyxl

from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup 
from aiogram.fsm.context import FSMContext 
from aiogram.filters.command import CommandStart   
from aiogram.filters.command import CommandStart  
from aiogram.filters.state import Filter   
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command 
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from class1 import Car, New_car, CarEncoder

API_TOKEN = '6773453600:AAGmMXq-MGKleUj0QX7_T65cu_PS4lfHAJc'
# API_TOKEN = '6519487700:AAFsMPqa-LhsW2NVxxsRlOvvogBvhgPD4HY'

class CarForm(StatesGroup): 
    waiting_for_model = State() 
    waiting_for_country = State() 
    waiting_for_year = State() 
    waiting_for_car_up = State() 
    waiting_for_spec = State() 
    waiting_for_car_id = State() 
    waiting_for_type = State()

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


#--------------------------------------------------------------------------------------------
# Функция добавления машины в JSON
def save_cars_to_file(cars, file_path):
    with open(file_path, "w") as file:
        json.dump(cars, file, cls=CarEncoder, indent=4)


# Функция чтения машины из JSON
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
    

# Просмотр списка машин(кол-во, бренды, специализации) 
def view_cars():
    print("\n===========================")
    print(f"Количество машин: {len(cars)}")
    unique_brands = set([car.model for car in cars.values()])
    print(f"Уникальные марки машин: {sorted(list(unique_brands))}")
    print("===========================")

    for car_type, car_list in cars.items():
        if car_type == "инженерные":
            print("\n===========================")
            unique_specializations = set([car.spec for car in car_list.values()])
            print(f"Уникальные специализации {car_type} машин: {sorted(list(unique_specializations))}")
            print("===========================")


# Удаление машины по id 
def remove_car(car_id):
    print("\n---------------------------")
    
    try:
        if car_id in cars:
            del cars[car_id]
            save_cars_to_file(cars, FILE_PATH)
            print("\n---------------------------")
            print("Машина успешно удалена.")
            print("---------------------------")
        else:
            print("\n!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!")
            print("Машины с таким ID нет в справочнике.")
            print("!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!")
    except ValueError:
        print("\n!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!")
        print("ID должен быть числом.")
        print("!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!")


# def to_list(self): 
#         return [self.car_id, self.year, self.country, self.model, self.car_up, self.spec] 
# class CarStorage: 
#     def __init__(self, file_name): 
#         self.car_list = [] 
#         self.next_id = 1 
#         self.file_name = file_name

# Выгрузка в EXEL
def save_to_excel(self): 
    pandas.read_json(FILE_PATH).to_excel(file_xlsx)

# Определение переменных
FILE_PATH = "cars.json"
cars = load_cars_from_file(FILE_PATH)
file_xlsx = "cars.xlsx"

#-------------------------------------------------------------

# Ветвление диалогов в боте
@dp.message(Command('start'))
async def start_adding_car(message: types.Message, state=FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text = 'simple'),
        types.KeyboardButton(text='special')
    )
    await message.answer("Какую машину вы хотите добавить?", reply_markup=builder.as_markup(resize_keyboard=True))


# Начало добавления обычной машины
@dp.message(F.text.lower() == 'simple')
async def send_simple(message: types.Message, state=FSMContext):
    await state.update_data(type=message.text)
    print(f"ТИП МАШИНЫ {type}")
    await state.set_state(CarForm.waiting_for_model)
    await message.answer("Добавим простую машину! Укажите марку: ")
    

# Добавление модели 
@dp.message(CarForm.waiting_for_model)
async def model_received(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await state.set_state(CarForm.waiting_for_country)
    await message.answer("Какая страна?")

    print(f"! Машина записана с ID - {car_id} !")
    cars[car_id] = main_car
    save_cars_to_file(cars, FILE_PATH)

    await message.answer("Машина записана в файл")
    await state.clear()
        
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text = 'simple'),
        types.KeyboardButton(text='special'),
        )
    builder.row(
        types.KeyboardButton(text='exel'),
        types.KeyboardButton(text='delete')
        )
    await message.answer(
        "Хотите добавить еще простую или специальную машину? Или выгрузить в EXEL?", 
        reply_markup=builder.as_markup(resize_keyboard=True)
        )
    
#начало добавления специальной машины
@dp.message(F.text.lower() == 'special')
async def send_special(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    global type
    type=message.text
    print(f"ТИП МАШИНЫ {type}")
    await state.set_state(CarForm.waiting_for_spec)
    await message.answer("Добавим специальную машину! Укажите спецализацию: ")
    return type

#добавление добавление спецализации
@dp.message(CarForm.waiting_for_spec)
async def spec_received(message: types.Message, state: FSMContext):
    await state.update_data(spec=message.text)
    await state.set_state(CarForm.waiting_for_car_up)
    await message.answer("Какая высота машины?")
    
#добавление высоты спец-машины 
@dp.message(CarForm.waiting_for_car_up)
async def car_up_received(message: types.Message, state: FSMContext):
    await state.update_data(car_up=message.text)
    await state.set_state(CarForm.waiting_for_model)
    await message.answer("Какая модель?")
    

#добавление страны 
@dp.message(CarForm.waiting_for_country)
async def country_received(message: types.Message, state: FSMContext):
    await state.update_data(country=message.text)
    await state.set_state(CarForm.waiting_for_year)
    await message.answer("Какой год выпуска?")

#добавление года выпуска
@dp.message(CarForm.waiting_for_year)
async def year_received(message: types.Message, state: FSMContext):
    global a
    if type == "simple":
        data = await state.get_data()
        car_id = len(cars) + 1
        model = data['model']
        country = data['country']
        year = message.text
        main_car = Car(car_id, year, country, model)
    elif type == "special":
        car_id = len(cars) + 1
        data = await state.get_data()
        model = data['model']
        country = data['country']
        year = message.text
        main_car = New_car(car_id, year, country, model, car_up, spec)

        
import pandas as pd
import pandas

# Конвертация в EXEL
@dp.message(F.text.lower() == 'exel')
async def send_exel(message: types.Message, state=FSMContext):
    print(f'тачка на прокачку {cars}')
        
    pandas.read_json("cars.json").to_excel("cars.xlsx")    

    await message.answer("Выгружаю в Exel, но это не точно...")

# Удаление машины по ID
@dp.message(F.text.lower() == 'delete')
async def send_car_id(message: types.Message, state=FSMContext):
    
    await state.set_state(CarForm.waiting_for_car_id)
    await message.answer("Укажите id, для удаления? ")

@dp.message(CarForm.waiting_for_car_id)
async def car_id_received(message: types.Message, state: FSMContext):
    await state.update_data(car_id=message.text)
    print(f"!!! {car_id} !!!")
    
    #remove_car(car_id)
    await message.answer(f"Машина с ID {car_id} типо удалена...")
    pandas.read_json("cars.json").to_excel("cars.xlsx")


#-------------------------------------------------------------

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())