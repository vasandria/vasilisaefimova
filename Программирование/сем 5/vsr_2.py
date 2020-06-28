import itertools


def fib(n):
    a, b = 1, 1
    f = [a]
    while b < n:
        f.append(b)
        a, b = b, a + b
    return f

    f = []
    for i in itertools.takewhile(lambda x: x < n, fib(n)):
        f.append(i)


print(fib(60))

if __name__ == "__main__":
    test = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    fib_list = fib(4)

    for i in range(0, len(fib_list) - 1):
        assert(fib_list[i] == test[i])
