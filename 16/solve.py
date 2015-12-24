#!/usr/bin/python3
import sys
from functools import reduce
from operator import mul

lines = list(line.strip() for line in sys.stdin if line.strip())

detected = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


database = {}
for line in lines:
    name, rest = line.split(': ', 1)
    database[name] = dict([(y[0], int(y[1])) for y in [x.split(': ') for x in rest.split(', ')]])


def matches(data, detected):
    for thing, value in data.items():
        if detected.get(thing) != value:
            return False

    return True

for sue, data in database.items():
    if matches(data, detected):
        print(sue, data)


def matches2(data, detected):
    for thing, value in data.items():
        if thing in ('cats', 'trees'):
            if detected.get(thing) >= value:
                return False

        elif thing in ('pomeranians', 'goldfish'):
            if detected.get(thing) <= value:
                return False

        elif detected.get(thing) != value:
            return False

    return True

for sue, data in database.items():
    if matches2(data, detected):
        print(sue, data)
