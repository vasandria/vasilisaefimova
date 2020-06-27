def sum_arithmetic_progression(a0, d, n):
    if n == 1:
        return a0
    else:
        return arithmetic_progression(a0, d, n) + sum_arithmetic_progression(a0, d, n - 1)


def arithmetic_progression(a0, d, n):
    if n == 1:
        return a0
    else:
        return arithmetic_progression(a0, d, n - 1) + d


print(sum_arithmetic_progression(1, 2, 6))
