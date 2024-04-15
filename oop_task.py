from class1 import Car
from class1 import New_car

cars = {}

def add_car():
    car_type = input("Введите тип машины (обычная/инженерная): ")

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
        carrying_capacity = input("Введите грузоподъемность машины: ")
        specialization = input("Введите специализацию машины: ")
        main_car = New_car(car_id, year, country, model, carrying_capacity, specialization)

    else:
        print("Неверный тип машины. Попробуйте еще раз.")
        return

    cars[car_id] = main_car

def view_cars():
    print(f"Количество машин: {len(cars)}")
    unique_brands = set([car.model for car in cars.values()])
    print(f"Уникальные марки машин: {sorted(list(unique_brands))}")

    for car_type, car_list in cars.items():
        if car_type == "инженерные":
            unique_specializations = set([car.specialization for car in car_list.values()])
            print(f"Уникальные специализации {car_type} машин: {sorted(list(unique_specializations))}")

while True:
    print("\nМеню:")
    print("1. Добавление машин.")
    print("2. Вывести все машины.")
    print("3. Программа завершена.")

    choice = input("Выберите опцию: ")

    if choice == "1":
        add_car()
    elif choice == "2":
        view_cars()
    elif choice == "3":
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")