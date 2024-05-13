import json

all_avto = {}


while True:
    avto = input("Введите название бренда, модель и год авто:\n""Введите Стоп: ")
    if avto == "Стоп":
        break
    brand, model, year = avto.split(",")
    all_avto.setdefault((brand, model, year), avto)

print("Список авто:")
for i, (brand, model, year) in enumerate(all_avto.keys(), 1):
    print(f"{i}. {all_avto[(brand, model, year)]}")

choice = input("Вы хотите удалить машину из списка? (да/нет): ")
if choice == "да":
    while True:
        choice_number = int(input("Введите номер машины из списка, которую вы хотите удалить: "))
        del all_avto[list(all_avto.keys())[choice_number - 1]]
        print("Машина под номером", choice_number, "удалена!\n",)
        print("Список авто после удаление:")
        for i, (key, value) in enumerate(all_avto.items(), 1):
                print(f"{i}. {key}: {value}")
else:
    print("Список сохранён!")
FILE_PATH = "all_avto.json"

