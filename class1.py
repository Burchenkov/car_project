
class Car:
    def __init__(self, year, country, model):
        self.year = year
        self.country = country
        self.model = model

    def get_year(self):
        return self.year

    def get_country(self):
        return self.country

    def get_model(self):
        return self.model
    
    def __getstate__(self) -> object:
        state = {}
        state["year"] = self.year
        state["country"] = self.country
        state["model"] = self.model
        return state
    
    def __setstate__(self, state: object):
        self.year = state["year"]
        self.country = state["country"]
        self.model = state["model"]

class New_car(Car):
    def __init__(self, year, country, model, car_up, spec):
        super().__init__(year, country, model)
        self.car_up = car_up
        self.spec = spec

    def get_car_up(self):
        return self.car_up

    def get_spec(self):
        return self.spec
    
    def __getstate__(self) -> object:
        state = {}
        state["spec"] = self.spec
        state["car_up"] = self.car_up
        return state
    
    def __setstate__(self, state: object):
        self.spec = state["spec"]
        self.car_up = state["car_up"]




    


