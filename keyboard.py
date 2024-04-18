# ИМПОРТ ДЛЯ ТГ-БОТА С 2 СТР ПО 13 СТР
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






@dp.message(Command('start'))   #Клавиши выбора авто с 31стр по 40 стр
async def start_adding_car(message: types.Message):
    
    kb = [
        [types.KeyboardButton(text='/simple')],
        [types.KeyboardButton(text='/special')]
        
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Какую машину хотите добавить?', reply_markup=keyboard)