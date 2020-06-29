def fibonacci(n):
    fib_list = []
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib1)
    return fib_list


a = int(input("Введите количество элементов ряда Фибоначчи: "))
print(fibonacci(a))

