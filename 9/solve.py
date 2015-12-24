#!/usr/bin/python3
import re
import sys

lines = list(line.strip() for line in sys.stdin if line.strip())

nodes = set()
graph = {}

def set_distance(node1, node2, distance):
    global nodes, graph

    nodes.add(node1)
    nodes.add(node2)

    graph[node1, node2] = distance
    graph[node2, node1] = distance


for line in lines:
    mo = re.match(r'^(?P<from>.+) to (?P<to>.*) = (?P<distance>\d+)', line)
    if not mo:
        raise Exception("line doesn't match: {}".format(line))

    set_distance(mo.group('from'), mo.group('to'), int(mo.group('distance')))


def find_path_length(current, left, func):
    global graph
    if not left:
        return 0

    minimum = None
    for node in left:
        if current:
            distance = graph.get((current, node))
            if distance is None:
                continue
        else:
            distance = 0

        l = find_path_length(node, left - {node}, func)
        if l is None:
            continue

        l += distance
        minimum = l if minimum is None else func(minimum, l)

    return minimum

print(find_path_length(None, nodes, min))
print(find_path_length(None, nodes, max))
