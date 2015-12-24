#!/usr/bin/python3
import sys
from functools import reduce
from operator import mul

lines = list(line.strip() for line in open(sys.argv[1]) if line.strip())

cache = {}

def find_all_groups(target, start_i):
    key = (target, start_i)
    if key not in cache:
        cache[key] = _find_all_groups(target, start_i)

    return cache[key]


def _find_all_groups(target, start_i):
    global weights
    if target == 0:
        return [set()]

    if target < 0 or start_i >= len(weights):
        return []

    all_solutions = []
    for i in range(start_i, len(weights)):
        weight = weights[i]
        for solution in find_all_groups(target - weight, i + 1):
            all_solutions.append(solution | set([weight]))

    return all_solutions


weights = [int(x) for x in lines]
#weights = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

def qe(g):
    return reduce(mul, g)

def group_key(g):
    return (len(g), qe(g))

def solve(num_groups):
    target_weight_per_group = sum(weights) // num_groups
    print(target_weight_per_group)
    possible_groups = list(find_all_groups(target_weight_per_group, 0))
    possible_groups.sort(key=group_key)
    print(len(possible_groups))
    for group1 in possible_groups:
        for group2 in [g for g in possible_groups if not g & group1]:
            for group3 in [g for g in possible_groups if not g & group1 & group2]:
                if num_groups == 3:
                    print(group1, group2, group3)
                    print(qe(group1))
                    return
                else:
                    for group4 in [g for g in possible_groups if not g & group1 & group2 & group3]:
                        print(group1, group2, group3, group4)
                        print(qe(group1))
                        return

solve(3)
solve(4)
