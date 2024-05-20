import json

class Car:
    def __init__(self, year, country, model, car_id):
        self.year = year
        self.country = country
        self.model = model
        self.car_id = car_id

class Specialized_car(Car):
    def __init__(self, year, country, model, car_id, car_up, specialization):
        super().__init__(year, country, model, car_id)
        self.car_up = car_up
        self.specialization = specialization

class CarEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Car, Specialized_car)):
            return obj.__dict__
        return super().default(obj)


    


