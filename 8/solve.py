#!/usr/bin/python3
import sys

lines = list(line.strip() for line in sys.stdin if line.strip())

total_code = 0
total_str = 0
total_repr = 0
for line in lines:
    total_code += len(line)
    total_str += len(eval(line))
    encoded_line = line.replace("\\", "\\\\").replace('"', '\\"')
    # the start and end quote would result in two more...
    total_repr += len(encoded_line) + 2

print(total_code - total_str)
print(total_repr - total_code)
