from class1 import Car
from class1 import New_car

mashina_obychnye = {}
mashina_inzhenernaya = {}

while True:
    id_mashiny = 1
    vid_mashiny = input("Введите тип машины (обычная / инженерная):\n")

    if vid_mashiny.lower() == "обычная":
        year = input("Введите год выпуска машины: \n")
        country = input("Введите страну выпуска машины:\n")
        model = input("Введите марку машины: \n")
        main_mashina = Car(year, country, model)
        mashina_obychnye[id_mashiny] = main_mashina
        id_mashiny += 1

    elif vid_mashiny.lower() == "инженерная":
        year = input("Введите год выпуска машины: \n")
        country = input("Введите страну выпуска машины:\n")
        model = input("Введите марку машины: \n")
        car_up = input("Введите грузоподъемность машины:\n")
        specialization = input("Введите специализацию машины:\n")
        main_mashina = New_car(year, country, model, car_up, specialization)
        mashina_inzhenernaya[id_mashiny] = main_mashina
        id_mashiny += 1

    else:
        print("Неверный тип машины. Попробуйте еще раз.")

    print("===================================================")
    print("Машина добавлена!")
    print(f"ID машины: {id_mashiny - 1}")
    print("===================================================")

    print("---------------------------------------------------")

    print("Список обычных машин:")
    for id_mashiny, main_mashina in mashina_obychnye.items():
        print(f"ID: {id_mashiny}")
        print(f"Год выпуска: {main_mashina.year}")
        print(f"Страна выпуска: {main_mashina.country}")
        print(f"Марка: {main_mashina.model}")

    print("---------------------------------------------------")

    print("Список инженерных машин:")
    for id_mashiny, main_mashina in mashina_inzhenernaya.items():
        print(f"ID: {id_mashiny}")
        print(f"Год выпуска: {main_mashina.year}")
        print(f"Страна выпуска: {main_mashina.country}")
        print(f"Марка: {main_mashina.model}")
        print(f"Грузоподъемность: {main_mashina.car_up}")
        print(f"Специализация: {main_mashina.specialization}")

    print("---------------------------------------------------")