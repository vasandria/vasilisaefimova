import numpy as np
from datetime import datetime

print("Для выполения операции умножения, матрицы A и B должны быть совместимы!")
n = int(input("Введите кол-во строк матрицы A и столбцов матрицы B: "))
m = int(input("Введите кол-во строк матрицы B и столбцов матрицы A: "))

print("Введите элементы матрицы А:")
a = np.empty((n, m))
for i in range(n):
    for j in range(m):
        a[i, j] = input()
print("матрица А:", a)


print("Введите элементы матрицы B:")
b = np.empty((m, n))
for i in range(m):
    for j in range(n):
        b[i, j] = input()
print("матрица B:", b)


print("А*B:")
start_time = datetime.now()
print(np.dot(a, b))

print('{} - время выполнения вычислений'.format(datetime.now() - start_time))
