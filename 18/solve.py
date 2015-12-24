#!/usr/bin/python3
import sys
from functools import reduce
from operator import mul

lines = list(line.strip() for line in open(sys.argv[1]) if line.strip())

field = [[1 if c == '#' else 0 for c in line] for line in lines]

def get_num_neighbours(x, y, field):
    n = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue

            nx = x + i
            ny = y + j
            if (nx < 0 or nx >= len(field[0]) or
                ny < 0 or ny >= len(field)):
                continue

            n += field[ny][nx]

    return n

def next_step(field, force_corners_on=False):
    result = [[0 for i in range(len(field[0]))] for j in range(len(field))]
    for y in range(len(field)):
        for x in range(len(field[0])):
            neighbours = get_num_neighbours(x, y, field)
            if (field[y][x] and neighbours in (2, 3)) or (not field[y][x] and neighbours == 3):
                result[y][x] = 1

    if force_corners_on:
        result[0][0] = 1
        result[-1][0] = 1
        result[0][-1] = 1
        result[-1][-1] = 1

    return result

def printit(field, size):
    print('\n'.join((''.join('*' if c else ' ' for c in row[:size]) for row in field[:size])))
    print('---')

original_field = field
for i in range(100):
    field = next_step(field)

print(sum(sum(row) for row in field))

field = original_field
for i in range(100):
    field = next_step(field, force_corners_on=True)

print(sum(sum(row) for row in field))
