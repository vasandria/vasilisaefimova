print("Введите длины сторон треугольника")
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2.0
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print("Площадь треугальника равна = ", s)
