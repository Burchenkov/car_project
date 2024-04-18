#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio

import pickle

from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import CommandStart
from aiogram.filters.command import CommandStart
from aiogram.filters.state import Filter
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from class1 import Car, New_car

# API_TOKEN = '6773453600:AAGmMXq-MGKleUj0QX7_T65cu_PS4lfHAJc'
API_TOKEN = "6519487700:AAFsMPqa-LhsW2NVxxsRlOvvogBvhgPD4HY"


class CarForm(StatesGroup):
    waiting_for_model = State()
    waiting_for_country = State()
    waiting_for_year = State()
    waiting_for_car_up = State()
    waiting_for_spec = State()
    type_vehicle = State()


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ------------------------------------------------------------------------
@dp.message(Command("start"))
async def start_adding_car(message: types.Message, state: FSMContext):
    await message.answer("Какую машину вы хотите добавить? simple/special")
    await state.set_state(CarForm.type_vehicle)

@dp.message(CarForm.type_vehicle)
async def choose_type(message: types.Message, state: FSMContext):
    text = message.text.lower()
    if text == "simple":
        await state.set_state(CarForm.waiting_for_model)
        await state.update_data(type_vehicle="simple")
        await message.answer("Добавим простую машину! Укажите марку: ")
    elif text == "special":
        await state.set_state(CarForm.waiting_for_spec)
        await state.update_data(type_vehicle="special")
        await message.answer("Добавим специальную машину! Укажите специализацию: ")
    else:
        await message.answer("Пожалуйста, выберите тип машины: 'simple' или 'special'.")



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
    model = data["model"]
    country = data["country"]
    year = message.text
    if data["type_vehicle"] == "special":
        spec = data["spec"]
        car_up = data["car_up"]
        a = New_car(year, country, model, spec, car_up)
    else:
        a = Car(year, country, model)

    with open("table.txt", "wb") as t:

        pickle.dump(a, t)

    await message.answer(
        f"Спасибо! Машина {country} {model} {year} года добавлена. Напищите simple/special чтобы добавить еще!"
    )
    await state.clear()
    await state.set_state(CarForm.type_vehicle)
# ------------------------------------------------------------------------

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
