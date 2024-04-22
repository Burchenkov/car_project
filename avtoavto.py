# + Добавил возможность добавление авто
# + Показ всех добаленных авто в списке (по сути ID)
# + Удаление авто из списка так же по ID
# + Осталось попытаться добавить все в Exel файл если получится 



all_avto = []

while True:
    avto = input("Введите название бренда, модель и год авто:\n""Введите Опции: ")
    if avto == "Опции":
        break
    avto_spisok = [avto]
    all_avto.append(avto_spisok)

print("Список авто:")
for i, avto in enumerate(all_avto, 1):
    print(f"{i}. {avto}")

choice = input("Вы хотите удалить машину из списка? (да/нет): ")
if choice == "да":
 while True:
    choice_number = int(input("Введите номер машины из списка, которую вы хотите удалить: "))
    del all_avto[choice_number - 1]
    print("Машина под номером", choice_number, "удалена!\n",)
    print("Список авто после удаление:")
    for i, avto in enumerate(all_avto, 1):
        print(f"{i}. {avto}")
        

else:
    print("Список сохранён!")


         






