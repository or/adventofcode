#!/usr/bin/python3
import re
import sys

lines = list(line.strip() for line in sys.stdin if line.strip())

def fun_or(a, b):
    return a | b

def fun_not(a):
    return ~a & 0xffff

def fun_and(a, b):
    return a & b

def fun_lshift(a, b):
    return (a << b) & 0xffff

def fun_rshift(a, b):
    return a >> b

def fun_id(a):
    return a

def get_input(x):
    if x.isdigit():
        return int(x)

    return x

def get_value(network, x):
    if isinstance(x, int):
        return x

    return evaluate(network, x)

def evaluate(network, output):
    global values
    if output not in values:
        info = network[output]
        operator = info[0]
        args = [get_value(network, x) for x in info[1:]]
        values[output] = operator(*args)

    return values[output]

values = {}
network = {}
for line in lines:
    mo = re.match(r'(?P<input1>\S+) -> (?P<output>\S+)', line)
    if not mo:
        mo = re.match(r'(?P<input1>\S+) (?P<operator>\S+) (?P<input2>\S+) -> (?P<output>\S+)', line)

    if not mo:
        mo = re.match(r'(?P<operator>NOT) (?P<input1>\S+) -> (?P<output>\S+)', line)

    if not mo:
        raise Exception("couldn't parse: {}".format(line))

    d = mo.groupdict()
    operator = locals()['fun_' + d.get('operator', 'id').lower()]

    if 'input2' in d:
        info = (operator, get_input(d['input1']), get_input(d['input2']))
    else:
        info = (operator, get_input(d['input1']))

    output = d['output']
    if output in network:
        raise Exception("multiple outputs on {}: {}".format(output, line))

    network[output] = info

solution1 = evaluate(network, 'a')
print(solution1)
network['b'] = (fun_id, solution1)
values = {}
solution2 = evaluate(network, 'a')
print(solution2)
