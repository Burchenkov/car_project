import json
from class1 import CarEncoder
from class1 import Car
from class1 import New_car

def save_cars_to_file(cars, file_path):
    with open(file_path, "w") as file:
        json.dump(cars, file, cls=CarEncoder, indent=4)

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
    
FILE_PATH = "cars.json"
cars = load_cars_from_file(FILE_PATH)

def add_car():
    print("\n---------------------------")
    car_type = input("Введите тип машины (обычная/инженерная): ")
    print("---------------------------")

    if car_type.lower() == "обычная":
        car_id = len(cars) + 1
        year = input("Введите год выпуска машины: ")
        country = input("Введите страну выпуска машины: ")
        model = input("Введите марку машины: ")
        main_car = Car(car_id, year, country, model)

    elif car_type.lower() == "инженерная":
        car_id = len(cars) + 1
        year = input("Введите год выпуска машины: ")
        country = input("Введите страну выпуска машины: ")
        model = input("Введите марку машины: ")
        car_up = input("Введите грузоподъемность машины: ")
        spec = input("Введите специализацию машины: ")
        main_car = New_car(car_id, year, country, model, car_up, spec)

    else:
        print("\n!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!")
        print("Неверный тип машины. Попробуйте еще раз.")
        print("!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!")
        return

    cars[car_id] = main_car
    save_cars_to_file(cars, FILE_PATH)

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

def remove_car():
    print("\n---------------------------")
    car_id = input("Введите ID удаляемой машины: ")
    print("---------------------------")
    try:
        car_id = int(car_id)
        if car_id in cars:
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

while True:
    print("\n===========================")
    print("\t   Меню:")
    print("1. Добавление машин")
    print("2. Вывести все машины")
    print("3. Удалить машину")
    print("4. Завершить программу.")
    print("===========================")

    choice = input("Выберите опцию: ")

    if choice == "1":
        add_car()
    elif choice == "2":
        view_cars()
    elif choice == "3":
        remove_car()
    elif choice == "4":
        break
    else:
        print("\n!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!")
        print("Некорректный выбор. Попробуйте снова.")
        print("!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!!=-=!")