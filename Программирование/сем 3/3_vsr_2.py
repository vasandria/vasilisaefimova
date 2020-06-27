print("Введите 10 чисел")
A = []
for _ in range(10):
    A.append(int(input()))

counter = {}

for elem in A:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {elem: count for elem, count in counter.items() if count > 1}
print(doubles)