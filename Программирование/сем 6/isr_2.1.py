def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


a = int(input("Введите количество элементов ряда Фибоначчи: "))
print(list(fibonacci(a)))