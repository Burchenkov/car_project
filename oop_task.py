from class1 import Car
from class1 import New_car

cars = {}
id_mashiny = 1

def add_car(id_mashiny):
    id_mashiny = id_mashiny
    vid_mashiny = input("Введите тип машины (обычная / инженерная):\n")

    if vid_mashiny.lower() == "обычная":
        year = input("Введите год выпуска машины: \n")
        country = input("Введите страну выпуска машины:\n")
        model = input("Введите марку машины: \n")
        main_mashina = Car(year, country, model)
    elif vid_mashiny.lower() == "инженерная":
        year = input("Введите год выпуска машины: \n")
        country = input("Введите страну выпуска машины:\n")
        model = input("Введите марку машины: \n")
        car_up = input("Введите грузоподъемность машины:\n")
        specialization = input("Введите специализацию машины:\n")
        main_mashina = New_car(year, country, model, car_up, specialization)
    else:
        print("Неверный тип машины. Попробуйте еще раз.")
        return
    
    cars[id_mashiny] = main_mashina
    id_mashiny += 1

def view_cars():
    for key in sorted(cars.keys()):
        print(f"Количество машин: {len(cars)}")
        unique_brands = set([car.model for car in cars.values()])
        print(f"Уникальные марки машин: {sorted(list(unique_brands))}")
        if key == "инженерные":
            unique_specializations = set([car.specialization for car in cars[key].values()])
            print(f"Уникальные специализации {key} машин: {sorted(list(unique_specializations))}")

while True:
    print("\nМеню:")
    print("1. Просмотр количества добавленных машин")
    print("2. Вывести все уникальные марки")
    print("3. Программа завершена.")

    choice = input("Выберите опцию: ")

    if choice == "1":
        add_car(id_mashiny)
    elif choice == "2":
        view_cars()
    elif choice == "3":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")