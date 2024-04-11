#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

API_TOKEN = '6773453600:AAGmMXq-MGKleUj0QX7_T65cu_PS4lfHAJc'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
i = 0
@dp.message(Command('start'))
async def send_welcome(message: types.Message):

    await message.reply("Привет! Я бот для ввода машин "
                         "Какую машину хотите добавить, напишите simple,или special? " 
                         "Если хотите выйти, наберите exit")

i = "on"
while True:

    @dp.message(Command('exit'))
    async def send_bye(message: types.Message):
        await message.reply("Пока пока, заходи если что!")
        i = "exit"
 
    if i == "exit"
        break


    @dp.message(Command('simple'))
    async def send_simple(message: types.Message):
        await message.reply("Вы добавили простую машину!")

    @dp.message(Command('special'))
    async def send_special(message: types.Message):
        type = "special"


    async def send_mark(message: types.Message):
        await message.reply("Введите марку")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())