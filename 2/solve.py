#!/usr/bin/python3
import sys

total = 0
total_ribbon = 0
for line in sys.stdin:
    line = line.strip()
    w, h, l = map(int, line.split('x'))
    sides = [w * h, h * l, w * l]
    sides.sort()
    dims = [w, h, l]
    dims.sort()
    total += 2 * sum(sides) + sides[0]
    total_ribbon += w * h * l + 2 * sum(dims[:2])

print(total)
print(total_ribbon)
