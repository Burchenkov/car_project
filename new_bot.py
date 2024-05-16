import asyncio
import json
import openpyxl

import pandas as pd
import pandas

from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup 
from aiogram.fsm.context import FSMContext 
from aiogram.filters.command import CommandStart   
from aiogram.filters.command import CommandStart  
from aiogram.filters.state import Filter   
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command 
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from class1 import Car, New_car, CarEncoder
from aiogram.types.input_file import FSInputFile


# my Telegram bot - @myCarListStoreBot
API_TOKEN = "6716836158:AAHxnBKSQOWqrdLtLITU7kfJPo6Y9xhwzdM" 

# API_TOKEN = '6773453600:AAGmMXq-MGKleUj0QX7_T65cu_PS4lfHAJc' - this is token 
# of Anton

# API_TOKEN = '6519487700:AAFsMPqa-LhsW2NVxxsRlOvvogBvhgPD4HY' - this is unlnown 
# token

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
    dict_keys = []
    for i in cars.keys():
        dict_keys.append(i)
    try:
        if car_id in dict_keys:
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
    builder.row(
    types.KeyboardButton(text='exel'),
    types.KeyboardButton(text='delete'),
    types.KeyboardButton(text='text')
    )
    # await message.answer("Какую машину вы хотите добавить?", reply_markup=builder.as_markup(resize_keyboard=True))
    print(cars)

    await message.answer(
        "Хотите добавить еще простую или специальную машину? Или выгрузить в EXEL или текст?", 
        reply_markup=builder.as_markup(resize_keyboard=True)
        )


#начало добавления специальной машины
@dp.message(F.text.lower() == 'special')
async def send_special(message: types.Message, state=FSMContext):
    # Пример обработки команды с установкой состояния
    await state.update_data(type=message.text)
    await state.set_state(CarForm.waiting_for_spec)
    await message.answer("Добавим специальную машину Укажите спецализацию: ")


#добавление спецализации
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


#начало добавления обычной машины
@dp.message(F.text.lower() == 'simple')
async def send_simple(message: types.Message, state=FSMContext):
    await state.update_data(type=message.text)
    print(f"ТИП МАШИНЫ {type}")
    await state.set_state(CarForm.waiting_for_model)
    await message.answer("Добавим простую машину Укажите марку: ")
    

#добавление модели 
@dp.message(CarForm.waiting_for_model)
async def model_received(message: types.Message, state: FSMContext):
    await state.update_data(model=message.text)
    await state.set_state(CarForm.waiting_for_country)
    await message.answer("Какая страна?")
    #car_id = len(cars) + 1


#добавление года выпуска и создание экземпляра класса
@dp.message(CarForm.waiting_for_year)
async def year_received(message: types.Message, state: FSMContext):
    car_id = len(cars) + 1
    data = await state.get_data()
    if data['type'] == "simple":
        model = data['model']
        country = data['country']
        year = message.text
        main_car = Car(car_id, year, country, model)
    elif data['type'] == "special":
        model = data['model']
        country = data['country']
        year = message.text
        car_up = data['car_up']
        spec = data['spec']
        main_car = New_car(car_id, year, country, model, car_up, spec)

    # print(f" Машина записана с ID - {car_id} !")
    cars[car_id] = main_car
    save_cars_to_file(cars, FILE_PATH)

    await message.answer(f"Машина записана в файл c ID {car_id}")
    await state.clear()
        
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text = 'simple'),
        types.KeyboardButton(text = 'special'),
        )
    builder.row(
        types.KeyboardButton(text = 'exel'),
        types.KeyboardButton(text = 'delete'),
        types.KeyboardButton(text = 'text')
        )
    await message.answer(
        "Хотите добавить еще простую или специальную машину? Или выгрузить в EXEL или текст?", 
        reply_markup=builder.as_markup(resize_keyboard=True)
        )


# Конвертация в EXEL
@dp.message(F.text.lower() == 'exel')
async def send_exel(message: types.Message, state=FSMContext):
    """эспорт из JSON файла в EXCEL"""
    print(f'тачка на прокачку {cars}')
    chat_id = message.chat.id

    JSON_FILE_NAME = "cars.json"
    EXCEL_FILE_NAME = "cars.xlsx"

    book = openpyxl.Workbook()
    sheet = book.active
    with open(JSON_FILE_NAME, 'r') as json_file:
        json_data = json.load(json_file)
    
    sheet['A1'] = 'Car ID'
    sheet['B1'] = 'YEAR'
    sheet['C1'] = 'COUNTRY'
    sheet['D1'] = 'MODEL'

    row = 2
    for key,value in json_data.items():
        sheet[row].value = value['car_id']
        sheet[row].value = value['year']
        sheet[row].value = value['country']
        sheet[row].value = value['model']
        row += 1

    book.save(EXCEL_FILE_NAME)
    book.close()
       
    document = FSInputFile('cars.xlsx') 
    await bot.send_document(chat_id, document) 

# Выгрузка в текстовый файл
@dp.message(F.text.lower() == 'text')
async def send_text(message: types.Message, state=FSMContext):
    chat_id = message.chat.id
    TEXT_FILE_NAME = "cars.txt"
    with open(TEXT_FILE_NAME, "w") as file:
        for car_id, car in cars.items():
            file.write(f"Car ID: {car_id}\n")
            file.write(f"Model: {car.model}\n")
            file.write(f"Country: {car.country}\n")
            file.write(f"Year: {car.year}\n")
            if isinstance(car, New_car):
                file.write(f"Specialization: {car.spec}\n")
                file.write(f"Car Up: {car.car_up}\n")
            file.write("\n")
    document = FSInputFile(TEXT_FILE_NAME) 
    await bot.send_document(chat_id, document) 

# Удаление машины по ID
@dp.message(F.text.lower() == 'delete')
async def send_car_id(message: types.Message, state=FSMContext):
    
    await state.set_state(CarForm.waiting_for_car_id)
    await message.answer("Укажите id, для удаления? ")

@dp.message(CarForm.waiting_for_car_id)
async def car_id_received(message: types.Message, state:FSMContext):
    await state.update_data(car_id=message.text)
    data = await state.get_data()
    id_to_del = int(data['car_id'])
    print(f"!!! {id_to_del} !!!")
    
    remove_car(id_to_del)
    await message.answer(f"Машина с ID {id_to_del} типо удалена...")
    pandas.read_json("cars.json").to_excel("cars.xlsx")


#-------------------------------------------------------------

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())