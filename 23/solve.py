#!/usr/bin/python3
import re
import sys
from functools import reduce
from operator import mul

lines = list(line.strip() for line in open(sys.argv[1]) if line.strip())

def parse(x):
    try:
        return int(x)
    except ValueError:
        pass

    return x

program = []
for line in lines:
    mo = re.match(r'^(inc|hlf|tpl|jmp|jie|jio) (a|b)?,? ?([+-]\d+)?', line)
    if not mo:
        raise Exception(line)

    opcode = tuple(parse(x) for x in mo.groups() if x is not None)
    program.append(opcode)


def inc(r):
    global registers, ip
    registers[r] += 1
    ip += 1


def hlf(r):
    global registers, ip
    registers[r] //= 2
    ip += 1


def tpl(r):
    global registers, ip
    registers[r] *= 3
    ip += 1


def jmp(o):
    global ip
    ip += o


def jie(r, o):
    global registers, ip
    if registers[r] % 2 == 0:
        ip += o
    else:
        ip += 1


def jio(r, o):
    global registers, ip
    if registers[r] == 1:
        ip += o
    else:
        ip += 1


registers = {'a': 0, 'b': 0}
ip = 0
while 0 <= ip < len(program):
    opcode = program[ip]
    locals()[opcode[0]](*opcode[1:])

print(registers['b'])

registers = {'a': 1, 'b': 0}
ip = 0
while 0 <= ip < len(program):
    opcode = program[ip]
    locals()[opcode[0]](*opcode[1:])

print(registers['b'])
