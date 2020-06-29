import pandas as pd
import numpy as nu

df = pd.read_csv('data3.csv', sep=';', encoding='utf-8', index_col="id")
print(df)
print(type(df))

xm = nu.mean(df['data'])  # среднее значение
xv = nu.var(df['data'])   # дисперсия
xs = nu.std(df['data'])   # cтандартное отклонение

print("среднее значение = ", xm, "\nдисперсия = ", xv, "\ncтандартное отклонение = ", xs)
