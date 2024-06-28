#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio

from aiogram import Router, filters
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove



API_TOKEN = '6773453600:AAGmMXq-MGKleUj0QX7_T65cu_PS4lfHAJc'

class CarForm(StatesGroup): #-----------
    waiting_for_brand = State() #-----------
    waiting_for_year = State() #-----------
    waiting_for_country = State() #-----------

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

from class1 import Car
list = []

@dp.message(Command("simple"))
async def cmd_simple(, state: FSMContext):
    await message.answer(
        text= "Выберите тип машины:"
      
    )
    await state.set_state(CarForm.waiting_for_brand)

# @dp.message(Command('start'))
# async def send_welcome(message: types.Message):

#     await message.answer("Привет! Я бот для ввода машин "
#                          "Какую машину хотите добавить, напишите simple,или special? " 
#                          "Если хотите выйти, наберите exit")


#     @dp.message(Command('exit'))
#     async def send_bye(message: types.Message):
#         await message.answer("Пока пока, заходи если что!")
        
 
# @dp.message(Command('simple'))
# async def send_simple(message: types.Message):
#     mark = None
#     yoc = None
#     country = None
    
#     await message.answer("Вы добавили простую машину! Укажите марку: ")
#     # list.append(Car(0,"", message.text))
#     # print(list[0])
#     @dp.message()
#     async def data(message: types.Message):
#         mark = message.text

#         await message.reply(f"Вы добавили марку {mark}, укажите год производства: ")

#         @dp.message()
#         async def data(message: types.Message):
#             yoc = int(message.text)

#             await message.reply(f"Вы указали год {yoc}, укажите страну производства: ")

#             @dp.message()
#             async def data(message: types.Message):
#                 country = message.text

#                 await message.reply(f"Вы добавили страну {country}, ура! Теперь наберите /simple или /special, чтобы добавить еще одну машину! ")


        

    # year = int(input("Введите год: \n"))
    # country = input("Введите страну: \n")
    # mark = input("Введите марку: \n")

    # list.append( Car(year, country, mark) )

    # print(list[0].country)


@dp.message(Command('special'))
async def send_special(message: types.Message):
    type = "special"


async def send_mark(message: types.Message):
    await message.reply("Введите марку")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())