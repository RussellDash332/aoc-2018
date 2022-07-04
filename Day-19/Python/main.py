import sys, time

def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]
def addi(reg, a, b, c):
    reg[c] = reg[a] + b
def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]
def muli(reg, a, b, c):
    reg[c] = reg[a] * b
def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]
def bani(reg, a, b, c):
    reg[c] = reg[a] & b
def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]
def bori(reg, a, b, c):
    reg[c] = reg[a] | b
def setr(reg, a, b, c):
    reg[c] = reg[a]
def seti(reg, a, b, c):
    reg[c] = a
def gtir(reg, a, b, c):
    reg[c] = int(a > reg[b])
def gtri(reg, a, b, c):
    reg[c] = int(reg[a] > b)
def gtrr(reg, a, b, c):
    reg[c] = int(reg[a] > reg[b])
def eqir(reg, a, b, c):
    reg[c] = int(a == reg[b])
def eqri(reg, a, b, c):
    reg[c] = int(reg[a] == b)
def eqrr(reg, a, b, c):
    reg[c] = int(reg[a] == reg[b])

ip = int(input().split()[1])
cmds = []
for line in sys.stdin:
    f, a, b, c = line.split()
    cmds.append([eval(f), int(a), int(b), int(c)])

debug = False

def simulate(val):
    reg = [0] * 6
    if val:
        BIG = 12 # 10551396
        reg, pos = [1, 2, 10, BIG, 0, BIG//2], 11
    else:
        pos = 0
    while pos < len(cmds):
        f, a, b, c = cmds[pos]
        if val and debug:
            print('ip=', ip, reg, '\tpos=', pos, '\t', f.__name__, a, b, c, end='\t\t')
        reg[ip] = pos
        f(reg, a, b, c)
        if val and debug:
            print('After:', reg)
            #time.sleep(0.5)
        pos = reg[ip] + 1
    if debug:
        print(f.__name__, a, b, c, reg)
    return reg[0]

print('Part 1:', simulate(0))

# My hypothesis is that the answer is the sum of divisors of BIG, since if BIG == 12 it gives 28
if debug:
    simulate(1)
# So let's just find the sum of divisors separately
BIG = 10551396
s, p = 0, 1
while p * p <= BIG:
    if BIG % p == 0:
        s += p + (BIG // p)
        if p == BIG // p:
            s -= p
    p += 1
print('Part 2:', s)