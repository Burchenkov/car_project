"""Телеграм БОТ 
the name for your bot:  myBotForCarListStore
username:  myCarListStoreBot
"""

import telebot
from telebot import types
from classes.Car import *

# константы
BOT_TOKEN = "6716836158:AAHxnBKSQOWqrdLtLITU7kfJPo6Y9xhwzdM"

# переменные
bot = telebot.TeleBot(BOT_TOKEN)
vin = ''
year = ''
country = ''
model = ''


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"""Выберите требуемую операцию(1,2,3,4): 
1. Добавление нового автомобиля в БД.
2. Вывод всех автомобилей.    
3. Удаление автомобиля из БД. 
Нужно будет знать ID в БД,
который можно будет найти в списке всех авто.
4. Сохранение список авто в Excel файл""")
  
@bot.message_handler(commands=['help'])
def start_message(message):
  bot.send_message(message.chat.id,"""1. Добавление нового автомобиля в БД.
2. Вывод всех автомобилей.    
3. Удаление автомобиля из БД. 
Нужно будет знать ID в БД,
который можно будет найти в списке всех авто.
4. Сохранение список авто в Excel файл""")

@bot.message_handler(content_types=['text'])
def add_auto(message):
    # Объявляем слушателя для получение текстовых сообшений, а так же метод их 
    # обработки. Для ведения диалога используем .
    if message.text == '1':
            bot.send_message(message.from_user.id, "Введите VIN")
            bot.register_next_step_handler(message, get_vin)
    else:
         bot.send_message(message.from_user.id, "Выберите номер функции. Для получения списка функций введите /help")

def get_vin(message):
    global vin
    vin = message.text
    bot.send_message(message.from_user.id, "Введите год выпуска")
    bot.register_next_step_handler(message, get_year)

def get_year(message):
    global year
    year = message.text
    bot.send_message(message.from_user.id, "Введите страну-производитель")
    bot.register_next_step_handler(message, get_country)

def get_country(message):
    global country
    country = message.text
    bot.send_message(message.from_user.id, "Ввдеите модель")
    bot.register_next_step_handler(message, get_model)

def get_model(message):
    global model
    model = message.text
    bot.send_message(message.from_user.id, 'Вы хотите добавить автомобиль: \nVIN:' + vin + '\nГод выпуска: ' + year + '\nПроизводство: ' + country + '\nМодель: ' + model)

oCar = Car(vin, year, country, model)

bot.polling(none_stop = True, interval=0)
