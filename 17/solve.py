#!/usr/bin/python3
import sys
from functools import reduce
from operator import mul

lines = list(line.strip() for line in sys.stdin if line.strip())

containers = []
for line in lines:
    containers.append(int(line))

solutions = []

def solve(n, containers, used=[]):
    global solutions
    if n == 0:
        solutions.append(used)
        return

    if n < 0:
        return

    if not containers:
        return

    if len(containers) == 1:
        if n in containers:
            solutions.append(used + [n])

        return

    for i in range(len(containers)):
        solve(n - containers[i], containers[i + 1:], used + [containers[i]])

solve(150, containers)
print(len(solutions))
print(min([len(s) for s in solutions]))
