#!/usr/bin/python3
import sys

def what_you_see(data):
    out = ''
    last = None
    for c in data:
        if last is None:
            last = c
            count = 1
        elif c == last:
            count += 1
        else:
            out += "{}{}".format(count, last)
            last = c
            count = 1

    out += "{}{}".format(count, last)

    return out

s = "1113122113"
for i in range(10):
    s = what_you_see(s)

print(len(s))

for i in range(50):
    s = what_you_see(s)

print(len(s))
