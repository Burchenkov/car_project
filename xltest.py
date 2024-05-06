# from openpyxl import Workbook
# from openpyxl import load_workbook

cars = [
    {
        "year": "2005",
        "country": "germany",
        "model": "bmw"
    },
    {
        "year": "2005",
        "country": "germany",
        "model": "bmw"
    }
]

# wb = Workbook()

# ws = wb.active

# ws.title = 'Cars'

# ws['A1'] = cars

# wb.save('D:\\Studing\car_project\demo.xlsx')

# print(ws['A1'])

import pandas as pd

df = pd.DataFrame(data=cars)

#convert into excel
df.to_excel("cars.xlsx", index=False)
print("Dictionary converted into excel...")