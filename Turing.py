__author__ = 'student'
import re

tape = {}
with open('tape6.txt') as f:
    line = f.read()
    for i, x in enumerate(line):
        tape[i] = x

rules = dict()
with open('rules6.txt') as f:
    for line in f.readlines():
        reg = re.match(r"^(.)q(\d+)->(.)(q\d+|STOP)(.)$", line)
        if reg == None:
            continue
        if reg.group(4) != 'STOP':
            new_condition = reg.group(4)[1:]
        else:
            new_condition = reg.group(4)
        if reg.group(1) not in rules:
            rules[reg.group(1)] = {}
        rules[reg.group(1)][reg.group(2)] = (reg.group(3), new_condition, reg.group(5))

q = 1
p = 1
while q != "STOP":
    symbol, q, movement = rules[tape[p]][str(q)]
    tape[p] = symbol
    if movement is 'R':
        p += 1
    elif movement == 'L':
        p -= 1
    if p not in tape:
        tape[p] = '_'   # new symbol

print(q, p)
for i in tape:
    print(tape[i], end='')