import sys

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
    # eqrr 4 0 2
    add_it = not avals
    break_it = reg[a] in avals
    if break_it:
        print('Part 2:', avals[-1])
        reg[-1] += 999
        return
    avals.append(reg[a])
    if add_it:
        print('Part 1:', avals[0])
    reg[c] = int(reg[a] == reg[b])

ip = int(input().split()[1])
cmds = []
for line in sys.stdin:
    f, a, b, c = line.split()
    cmds.append([eval(f), int(a), int(b), int(c)])

avals = []
def simulate():
    reg = [0] * 6
    pos = 0
    while pos < len(cmds):
        f, a, b, c = cmds[pos]
        reg[ip] = pos
        f(reg, a, b, c)
        pos = reg[ip] + 1
    return reg[0]

def simulate_optimized(BIG):                    # the big number that differentiates your test case with others
    avals = []
    reg = [0, 65536, 0, 0, 0]                   # 5 values is enough in this case
    reg[4] = BIG                                # seti BIG 3 4
    while True:
        reg[2] = reg[1] & 255                   # bani 1 255 2
        reg[4] += reg[2]                        # addr 4 2 4
        reg[4] &= 16777215                      # bani 4 16777215 4
        reg[4] *= 65899                         # muli 4 65899 4
        reg[4] &= 16777215                      # bani 4 16777215 4
        if 256 > reg[1]:                        # gtir 256 1 2, addr 2 5 5
            # Print answer
            if not avals:
                print('Part 1:', reg[4])
            if reg[4] in avals:
                print('Part 2:', avals[-1])
                return
            avals.append(reg[4])

            reg[2] = 1
            if reg[4] == reg[0]:                # seti 27 7 5, eqrr 4 0 2, addr 2 5 5
                break                           # HALT
            else:
                reg[2] = 0                      # seti 5 6 5
                reg[1] = reg[4] | 65536         # bori 4 65536 1
                reg[4] = BIG                    # seti BIG 3 4
        else:
            reg[2] = 0                          # addr 2 5 5, addi 5 1 5, seti 0 1 2
            reg[1] = reg[2] = reg[1] // 256     # optimize the chunk below
            '''
            while True:
                reg[3] = 256*(reg[2] + 1)       # addi 2 1 3, muli 3 256 3
                if reg[3] > reg[1]:             # gtrr 3 1 3, addr 3 5 5
                    reg[3] = 1                  # seti 25 2 5
                    reg[1] = reg[2]             # setr 2 3 1, seti 7 9 5
                    break                       # back to the outer while loop
                else:
                    reg[3] = 0                  # addi 5 1 5
                    reg[2] += 1                 # addi 2 1 2, seti 17 0 5
            '''

# The halting criteria is eqrr 4 0 2, as long as reg[4] != reg[0], the program will not halt
#simulate()
simulate_optimized(2024736)