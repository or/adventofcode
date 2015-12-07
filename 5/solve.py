#!/usr/bin/python3
import re
import sys

lines = list(line.strip() for line in sys.stdin)

nice = 0
for line in lines:
    vowels = re.findall('[aeuio]', line)
    if len(vowels) < 3:
        continue

    got_one = False
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            got_one = True
            break

    if not got_one:
        continue

    if any(x in line for x in ('ab', 'cd', 'pq', 'xy')):
        continue

    nice += 1

print(nice)

nice = 0
for line in lines:
    got_one = False
    for i in range(0, len(line) - 2):
        if line[i] + line[i + 1] in line[i + 2:]:
            got_one = True
            break

    if not got_one:
        continue

    got_one = False
    for i in range(0, len(line) - 2):
        if line[i] == line[i + 2]:
            got_one = True
            break

    if not got_one:
        continue

    nice += 1

print(nice)
