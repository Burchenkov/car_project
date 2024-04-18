class Car:
    def __init__(self, idm, year, country, model):
        self.idm = idm
        self.year = year
        self.country = country
        self.model = model

    def get_idm(self):
        return self.idm

    def get_year(self):
        return self.year

    def get_country(self):
        return self.country

    def get_model(self):
        return self.model

class New_car(Car):
    def __init__(self, idm, year, country, model, car_up, specialization):
        super().__init__(idm, year, country, model)
        self.car_up = car_up
        self.specialization = specialization

    def get_car_(self):
        return self.car_up

    def get_specialization(self):
        return self.specialization