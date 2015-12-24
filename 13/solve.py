#!/usr/bin/python3
import re
import sys
from itertools import permutations

lines = list(line.strip() for line in sys.stdin if line.strip())

nodes = set()
graph = {}
for line in lines:
    mo = re.match(r'^(.+) would (lose|gain) (\d+) happiness units by sitting next to (.+)\.$', line)
    name1, kind, units, name2 = mo.groups()
    units = int(units)
    if kind == 'lose':
        units *= -1

    nodes.add(name1)
    nodes.add(name2)
    graph[name1, name2] = units

def solve(nodes):
    global graph
    nodes = list(nodes)

    first = nodes.pop(0)
    max_happiness = 0
    for rest in permutations(nodes):
        happiness = 0
        order = (first,) + rest
        for i in range(len(order)):
            happiness += graph.get((order[i], order[(i + 1) % len(order)]), 0)
            happiness += graph.get((order[i], order[(i + len(order) - 1) % len(order)]), 0)

        max_happiness = max(max_happiness, happiness)

    return max_happiness

print(solve(nodes))
print(solve(nodes | set(['moi'])))
