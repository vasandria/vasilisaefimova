print("Введите 10 чисел")
A = []
unique = []
for i in range(10):
    A.append(int(input()))
for i in A:
    if A.count(i) == 1:
        unique.append(i)
print(unique)
