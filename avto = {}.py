all_avto = {}

while True:
    avto = input("Введите название бренд авто:\n""Введите Стоп: ")
    if avto == "Стоп":
        break
    brand = input("Введите название модель:\n""Введите Стоп: ")
    year = input("Введите год авто:\n""Введите Стоп: ")
    all_avto[(avto, brand, year)] = f"{avto} {brand} {year}"

print("Список авто:")
for i, (key, value) in enumerate(all_avto.items(), 1):
    print(f"{i}. {value}")

choice = input("Вы хотите удалить машину из списка? (да/нет): ")
if choice == "да":
    while True:
        choice_number = int(input("Введите номер машины из списка, которую вы хотите удалить: "))
        del all_avto[list(all_avto.keys())[choice_number - 1]]
        print("Машина под номером", choice_number, "удалена!\n",)
        print("Список авто после удаление:")
        for i, (key, value) in enumerate(all_avto.items(), 1):
            print(f"{i}. {value}")
else:
    print("Список сохранён!")

