import sys

samples = []
while True:
    bef = input().strip()
    if bef:
        opcode, a, b, c = map(int, input().split())
        after = input().strip()
        bef = eval(bef.split(':')[-1])
        after = eval(after.split(':')[-1])
        samples.append([bef, after, opcode, a, b, c])
        input()
    else:
        input()
        break
cmds = []
for line in sys.stdin:
    cmds.append(list(map(int, line.split())))

def addr(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a] + reg[b]
    return reg

def addi(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a] + b
    return reg

def mulr(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a] * reg[b]
    return reg

def muli(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a] * b
    return reg

def banr(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a] & reg[b]
    return reg

def bani(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a] & b
    return reg

def borr(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a] | reg[b]
    return reg

def bori(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a] | b
    return reg

def setr(reg, a, b, c):
    reg = reg.copy()
    reg[c] = reg[a]
    return reg

def seti(reg, a, b, c):
    reg = reg.copy()
    reg[c] = a
    return reg

def gtir(reg, a, b, c):
    reg = reg.copy()
    reg[c] = int(a > reg[b])
    return reg

def gtri(reg, a, b, c):
    reg = reg.copy()
    reg[c] = int(reg[a] > b)
    return reg

def gtrr(reg, a, b, c):
    reg = reg.copy()
    reg[c] = int(reg[a] > reg[b])
    return reg

def eqir(reg, a, b, c):
    reg = reg.copy()
    reg[c] = int(a == reg[b])
    return reg

def eqri(reg, a, b, c):
    reg = reg.copy()
    reg[c] = int(reg[a] == b)
    return reg

def eqrr(reg, a, b, c):
    reg = reg.copy()
    reg[c] = int(reg[a] == reg[b])
    return reg

funcs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

p1 = 0
for sample in samples:
    bef, after, opcode, a, b, c = sample
    ok_funcs = []
    for f in funcs:
        if f(bef, a, b, c) == after:
            ok_funcs.append(f.__name__)
    p1 += (len(ok_funcs) >= 3)
print('Part 1:', p1)

possible = {}
for i in range(16):
    possible[i] = set(funcs)
for sample in samples:
    bef, after, opcode, a, b, c = sample
    ok_funcs = set()
    for f in possible[opcode]:
        if f(bef, a, b, c) == after:
            ok_funcs.add(f)
    possible[opcode] = ok_funcs

deduced = [False] * 16
while sum(map(len, possible.values())) != len(possible):
    idx, selected = None, None
    for i in possible:
        if len(possible[i]) == 1 and not deduced[i]:
            deduced[i] = True
            idx, selected = i, list(possible[i])[0]
            break
    for i in possible:
        if i != idx and selected in possible[i]:
            possible[i].remove(selected)
for i in possible:
    possible[i] = list(possible[i])[0]
reg = [0, 0, 0, 0]
for opcode, a, b, c in cmds:
    reg = possible[opcode](reg, a, b, c)
print('Part 2:', reg[0])