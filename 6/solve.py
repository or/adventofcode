#!/usr/bin/python3
import re
import sys

lines = list(line.strip() for line in sys.stdin)

grid = [[0 for i in range(1000)] for j in range(1000)]
num_on = 0
grid2 = [[0 for i in range(1000)] for j in range(1000)]
sum_brightness = 0


def toggle(x, y):
    global grid, grid2, num_on, sum_brightness
    if grid[y][x]:
        num_on -= 1
    else:
        num_on += 1

    grid[y][x] = not grid[y][x]

    grid2[y][x] += 2
    sum_brightness += 2


def turn_on(x, y):
    global grid, grid2, num_on, sum_brightness
    if not grid[y][x]:
        num_on += 1
        grid[y][x] = True

    grid2[y][x] += 1
    sum_brightness += 1


def turn_off(x, y):
    global grid, grid2, num_on, sum_brightness
    if grid[y][x]:
        num_on -= 1
        grid[y][x] = False

    if grid2[y][x]:
        sum_brightness -= 1
        grid2[y][x] -= 1


for line in lines:
    mo = re.match(r'^(?P<command>turn on|turn off|toggle) (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)', line)
    if not mo:
        continue

    d = mo.groupdict()
    f = locals()[d['command'].replace(' ', '_')]
    for x in range(int(d['x1']), int(d['x2']) + 1):
        for y in range(int(d['y1']), int(d['y2']) + 1):
            f(x, y)

print(num_on)
print(sum_brightness)
