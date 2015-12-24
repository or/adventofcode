#!/usr/bin/python3
import re
import sys
from functools import reduce
from operator import mul

lines = list(line.strip() for line in open(sys.argv[1]) if line.strip())

rules = []
for line in lines:
    if '=>' not in line:
        break

    rule, repl = line.split(' => ')
    rules.append((rule, repl))

molecule = lines[-1]

def apply_all(molecule, rules):
    results = set()
    for rule, repl in rules:
        for match in re.finditer(rule, molecule):
            result = molecule[:match.start()] + repl + molecule[match.end():]
            results.add(result)

    return results

results = apply_all(molecule, rules)
print(len(results))

unconsumables = ['Ar', 'Ca', 'R', 'Si', 'Th', 'Y']
max_unconsumables = [molecule.count(x) for x in unconsumables]
current = set(['e'])
seen = set()
steps = 0
while current:
    print(len(current))
    next_set = set()
    steps += 1
    for m in current:
        tmp = apply_all(m, rules)
        if 'e' in tmp:
            print(steps)
            sys.exit(0)

        next_set |= tmp

    current = next_set - seen
    seen |= current

    continue
    current = set()
    for m in next_set:
        bad = False
        for i in range(len(unconsumables)):
            if m.count(unconsumables[i]) > max_unconsumables[i]:
                bad = True
                break

        if not bad:
            current.add(m)
