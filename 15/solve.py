#!/usr/bin/python3
import sys
from functools import reduce
from operator import mul

lines = list(line.strip() for line in sys.stdin if line.strip())

ingredients = []
for line in lines:
    ingredient, rest = line.split(': ')
    props = [int(x.split(' ')[1]) for x in rest.split(', ')]
    ingredients.append(props)

ingredients_without_calories = []
for line in lines:
    ingredient, rest = line.split(': ')
    props = [int(x.split(' ')[1]) for x in rest.split(', ') if not x.startswith('calories')]
    ingredients_without_calories.append(props)

def limited_partitions(n, size):
    if size == 0:
        yield []
        return

    if size == 1:
        yield [n]
        return

    for i in range(0, n + 1):
        for p in limited_partitions(n - i, size - 1):
            yield [i] + p


def calc(weights, ingredients):
    props = [0] * len(ingredients[0])
    for i in range(len(ingredients)):
        for p in range(len(ingredients[0])):
            props[p] += ingredients[i][p] * weights[i]

    return reduce(mul, [max(0, x) for x in props])

def solve(ingredients, total):
    best = 0
    for partition in limited_partitions(total, len(ingredients)):
        best = max(best, calc(partition, ingredients))

    return best

print(solve(ingredients_without_calories, 100))

def calc2(weights, ingredients):
    props = [0] * len(ingredients[0])
    for i in range(len(ingredients)):
        for p in range(len(ingredients[0])):
            props[p] += ingredients[i][p] * weights[i]

    if props[-1] != 500:
        return 0

    return reduce(mul, [max(0, x) for x in props[:-1]])

def solve2(ingredients, total):
    best = 0
    for partition in limited_partitions(total, len(ingredients)):
        best = max(best, calc2(partition, ingredients))

    return best

print(solve2(ingredients, 100))
