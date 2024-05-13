import json

class Car:
    def __init__(self, car_id, year, country, model):
        self.year = year
        self.country = country
        self.model = model
        self.car_id = car_id


class New_car(Car):
    def __init__(self, car_id, year, country, model, car_up, specialization):
        super().__init__(car_id, year, country, model)
        self.car_up = car_up
        self.specialization = specialization


class CarEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Car, New_car)):
            return obj.__dict__
        return super().default(obj)



    


