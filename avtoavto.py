all_avto = []

avto = input("Введите название бренда, модель и год авто: ") 
avto_spisok = [avto]

avto2 = input("Введите название бренда, модель и год авто: ")
avto_spisok2 = [avto2]

if avto2 in avto_spisok:
        print("Уже есть такая машина")
else:
        print("Вы добавили новое авто", avto2)
all_avto = [avto + avto2]
# if avto and avto2 == "Exit":
choice = input("Вы хотите удалить машину из списка? (да/нет): ")
if choice == "да":
    index = input("Введите данные машины, которую вы хотите удалить: ")
    all_avto = [avto,avto2]
    all_avto.remove(index)
    print("Машина", index , "удалена!")
else:
    print("Список сохранён!")
         






