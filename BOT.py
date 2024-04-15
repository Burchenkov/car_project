#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command 
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6773453600:AAGmMXq-MGKleUj0QX7_T65cu_PS4lfHAJc'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

from class1 import Car
list = []

@dp.message(Command('start'))
async def send_welcome(message: types.Message):

    await message.answer("Привет! Я бот для ввода машин "
                         "Какую машину хотите добавить, напишите simple,или special? " 
                         "Если хотите выйти, наберите exit")


    @dp.message(Command('exit'))
    async def send_bye(message: types.Message):
        await message.answer("Пока пока, заходи если что!")
        
 
@dp.message(Command('simple'))
async def send_simple(message: types.Message):
    marks = None
    yoc = None
    country = None
    
    await message.answer("Вы добавили простую машину! Укажите марку: ")
    # list.append(Car(0,"", message.text))
    # print(list[0])
    @dp.message()
    async def data(message: types.Message, this_marks, yoc, country):
        this_marks = marks

        await message.reply(f"Вы добавили марку {marks}")

        

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