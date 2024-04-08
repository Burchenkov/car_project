#Пример 1 (сам)

"""#Словари для хранения уникальных марок и специализаций
unique_brands = set()
unique_specializations = set()
machines = []

while True:
    print("\nМеню:")
    print("1. Просмотр количества добавленных машин")
    print("2. Вывести все уникальные марки")
    print("3. Программа завершена.")

    choice = input("Выберите опцию: ")

    if choice == "1":
        brand = input("Введите марку машины: ")
        specialization = input("Введите специализацию машины: ")
        machines.append((brand, specialization))
        unique_brands.add(brand)
        unique_specializations.add(specialization)
        print("Машина успешно добавлена!")
    elif choice == "1":
        print(f"Количество добавленных машин: {len(machines)}")
    elif choice == "2":
        print("Уникальные марки машин:")
        for brand in unique_brands:
            print(brand)
    elif choice == "3":
        print("Уникальные специализации машин:")
        for specialization in unique_specializations:
            print(specialization)
    elif choice == "4":
        print("Программа завершена.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")"""

#Пример 2 (Честно спиз***ое)
"""def view_cars():
    for key in sorted(cars.keys()):
        print(f"Количество {key} машин: {len(cars[key])}")
        unique_brands = set([car.марка for car in cars[key].values()])
        print(f"Уникальные марки {key} машин: {sorted(list(unique_brands))}")
        if key == "инженерные":
            unique_specializations = set([car.специализация for car in cars[key].values()])
            print(f"Уникальные специализации {key} машин: {sorted(list(unique_specializations))}")"""