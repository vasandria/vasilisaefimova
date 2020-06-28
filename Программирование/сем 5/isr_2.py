import itertools


def func(n):
    def fib():
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b

    f = []
    for i in itertools.takewhile(lambda x: x < n, fib()):
        f.append(i)
    return f


print(func(40))


if __name__ == "__main__":
    test = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    fib_list = func(7)
    for i in range(0, str(fib_list) - 1):
        assert(fib_list[i] == test[i])
