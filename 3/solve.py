#!/usr/bin/python3
import sys

data = sys.stdin.read().strip()

seen = set([(0, 0)])
x, y = 0, 0
for d in data:
    if d == '<':
        x -= 1
    elif d == '>':
        x += 1
    elif d == '^':
        y -= 1
    elif d == 'v':
        y += 1

    seen.add((x, y))

print(len(seen))

seen = set([(0, 0)])
x, y = [0, 0], [0, 0]
ind = 0
for d in data:
    if d == '<':
        x[ind] -= 1
    elif d == '>':
        x[ind] += 1
    elif d == '^':
        y[ind] -= 1
    elif d == 'v':
        y[ind] += 1

    seen.add((x[ind], y[ind]))
    ind = 1 - ind

print(len(seen))
