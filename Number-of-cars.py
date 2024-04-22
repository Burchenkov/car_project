import openpyxl

# Добавление класса

# Обычное авто
class Car:
    def __init__(self, car_id, year, country, brand):
        self.car_id = car_id
        self.year = year
        self.country = country
        self.brand = brand

# Инженерное авто
class EngineeringCar(Car):
    def __init__(self, car_id, year, country, brand, payload_capacity, specialization):
        super().__init__(car_id, year, country, brand)
        self.payload_capacity = payload_capacity
        self.specialization = specialization


    def to_list(self):
        return [self.car_id, self.year, self.country, self.brand, self.payload_capacity, self.specialization]
class CarStorage:
    def __init__(self, file_name):
        self.car_list = []
        self.next_id = 1
        self.file_name = file_name

    def add_cars(self, car):
        # Проверяем, существует ли уже такой ID в списке машин
        if any(c.id == car.id for c in self.car_list):
            car.id = self.next_id  # Присваиваем новый уникальный ID
            self.next_id += 1

        self.car_list.append(car)

# Добавление авто
    def add_car(self):
        year = input("Введите год выпуска машины: ")
        country = input("Введите страну производства: ")
        brand = input("Введите марку машины: ")
        payload_capacity = input("Введите грузоподъемность: ")
        specialization = input("Введите специализацию: ")

        car_id = self.next_id
        self.next_id += 1

        car = EngineeringCar(car_id, year, country, brand, payload_capacity, specialization)
        self.car_list.append(car)
        print("Машина успешно добавлена.")

# Функция добавления машину в excel
    def save_to_excel(self):
        wb = openpyxl.load_workbook(self.file_name)
        ws = wb.active

        for car in self.car_list:
            ws.append(car.to_list())

        wb.save(self.file_name)
        print(f"Данные успешно сохранены в файл {self.file_name}")

# Поиск авто по ID
    def find_car_by_id(self, car_id):
        # Код поиска машины по ID
        for car in self.car_list:
            if car.car_id == car_id:
                return car
        return None

# Пример использования
car_storage = CarStorage("user_cars_data.xlsx")

while True:
    user_input = input("Хотите добавить новую машину? (да/нет): ")
    if user_input.lower() != 'да':
        break

    car_storage.add_car()

car_storage.save_to_excel()

# функция для удаления авто по ID
def remove_car(self, car_id):
    car = self.find_car_by_id(car_id)
    if car is not None:
        self.car_list.remove(car)
        print(f"Машина с ID {car_id} успешно удалена.")
    else:
        print("Машина с указанным ID не найдена.")


while True:
    search_id = int(input("Введите ID машины для поиска: "))
    found_car = car_storage.find_car_by_id(search_id)

    if found_car is not None:
        print(f"Машина найдена - Марка: {found_car.brand}, Год выпуска: {found_car.year}")
    else:
        print("Машина не найдена.")

# сообщение "Хотите ли вы удалить авто " + "Найти машину по ID"
    found_car = car_storage.find_car_by_id(search_id)

    if found_car is not None:
       print(f"Машина найдена - Марка: {found_car.brand}, Год выпуска: {found_car.year}")
    choice_remove = input("Хотите удалить эту машину? (да/нет): ")
    if choice_remove.lower() == 'да':
        car_storage.remove_car(search_id)
    else:
       print("Машина не найдена.")

    choice = input("Хотите ли вы продолжить поиск? (да/нет): ")
    if choice.lower() != 'да':
        break
