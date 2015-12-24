#!/usr/bin/python3
import json
import sys

data = json.load(sys.stdin)

def sum_up(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return 0
    elif isinstance(data, list):
        return sum(map(sum_up, data))
    elif isinstance(data, dict):
        return sum(map(sum_up, data.values()))
    else:
        raise Exception(type(data))


def sum_up2(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return 0
    elif isinstance(data, list):
        return sum(map(sum_up2, data))
    elif isinstance(data, dict):
        if 'red' in data.values():
            return 0

        return sum(map(sum_up2, data.values()))
    else:
        raise Exception(type(data))


print(sum_up(data))
print(sum_up2(data))
