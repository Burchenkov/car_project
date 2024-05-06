cars = {}

def add_car(brand, model, year):
    id = 1
    if len(cars) == 0:
        cars[f'car_{id}'] = {
        'id': id,
        'brand': brand,
        'model': model,
        'year': year
        }
    else:
        for i in cars.keys():
            if id < cars[i]['id']:
                id = cars[i]['id']
        cars[f'car_{id}'] = {
        'id': id,
        'brand': brand,
        'model': model,
        'year': year
        }
        id += 1
    

def show_cars():
    print(cars)
