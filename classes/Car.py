class Car:
    """Класс создает объекты-автомобили."""
    def __init__(self, car_ID, year, country, model):
        self.car_ID = car_ID
        self.year = year
        self.country = country
        self.model = model

    def __str__(self):
        return (f"VIN: {self.car_ID}, Год выпуска: {self.year}, Страна производства: {self.country}, Модель: {self.model}")
