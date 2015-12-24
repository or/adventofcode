#!/usr/bin/python3
from functools import reduce
from itertools import product
from operator import mul


def get_factors(n):
    factors = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p

        if e:
            factors.append((p, e))

        if p == 2:
            p = 3
        else:
            p += 2

    if n > 1:
        factors.append((n, 1))

    return factors


def get_sum_divisors(n):
    factors = get_factors(n)
    s = 0

    exp_choices = [list(range(e + 1)) for x, e in factors]
    for vector in product(*exp_choices):
        if len(vector):
            s += reduce(mul, [factors[i][0] ** vector[i] for i in range(len(factors))])
        else:
            s += 1

    return s


def solve(value):
    i = 1
    while True:
        if get_sum_divisors(i) * 10 >= value:
            return i

        i += 1

value = 29000000
#print(solve(value))

def get_sum_divisors2(n):
    factors = get_factors(n)
    s = 0

    exp_choices = [list(range(e + 1)) for x, e in factors]
    for vector in product(*exp_choices):
        if len(vector):
            d = reduce(mul, [factors[i][0] ** vector[i] for i in range(len(factors))])
        else:
            d = 1

        if n // d <= 50:
            s += d

    return s


def solve2(value):
    i = 1
    while True:
        if get_sum_divisors2(i) * 11 >= value:
            return i

        i += 1


value = 29000000
print(solve2(value))
