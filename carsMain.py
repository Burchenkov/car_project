# программа для создания списка автомобилей, удаления записей из этого списка
# экспорт в JSON, при необходимости эскпорт в Excel
# тестовые изменения

import json
import openpyxl
from classes.Car import *


def save(data: dict, file_name: str) -> None:
    """принимаеи словарь, принимаем имя файла, записываем в формате
    JSON в файл"""
    with open(file_name, 'w') as file:
        json.dump(cars, file)


def print_dictionary(data: dict):
    """принимаем словарь, выводим в терминал в красивом виде"""
    for key, value in data.items():
        print(f"Base ID: {key}")
        print(f"{value}")


def save_to_excel():
    """эспорт из JSON файла в EXCEL"""
    book = openpyxl.Workbook()
    sheet = book.active
    with open(JSON_FILE_NAME, 'r') as json_file:
        json_data = json.load(json_file)
    
    sheet['A1'] = 'ID'
    sheet['B1'] = 'Car ID'
    sheet['C1'] = 'YEAR'
    sheet['D1'] = 'COUNTRY'
    sheet['E1'] = 'MODEL'

    row = 2
    for key,value in json_data.items():
        sheet[row][0].value = key
        sheet[row][1].value = value['car_id']
        sheet[row][2].value = value['year']
        sheet[row][3].value = value['country']
        sheet[row][4].value = value['model']
        row += 1

    book.save(EXCEL_FILE_NAME)
    book.close()


# константы
JSON_FILE_NAME = "data.json"
EXCEL_FILE_NAME = "data.xlsx"

save_to_excel()
