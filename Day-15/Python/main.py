import sys
from copy import deepcopy
from collections import deque

INIT_HP = 200
dirs = ((-1, 0), (0, -1), (0, 1), (1, 0))
debug = False

M = []
UNITS = []
for line in sys.stdin:
    line = list(line.strip())
    for i in range(len(line)):
        if line[i] in 'GE':
            UNITS.append([len(M), i, INIT_HP, line[i]])
    M.append(line)

def draw(m, units):
    m2 = deepcopy(m)
    for r, c, h, u in units:
        if h > 0:
            m2[r][c] = ['\033[92m', '\033[91m'][int(u == 'G')] + m2[r][c] + '\033[0m'
    print('\n'.join(map(lambda x: ''.join(x), m2)))

def valid(r, c):
    return 0 <= r <= len(M) - 1 and 0 <= c <= len(M[0]) - 1

def simulate(dmg):
    m, units = deepcopy(M), deepcopy(UNITS)
    rd = 0
    while len(set(map(lambda x: x[-1], units))) != 1:
        units.sort()
        
        if debug:
            print('ROUND', rd + 1)
        
        for i in range(len(units)):
            r, c, hp, u = units[i]
            if hp <= 0:
                continue
            in_range, attack = set(), set()
            for j in range(len(units)):
                r2, c2, hp2, u2 = units[j]
                if hp2 <= 0:
                    continue
                if u != u2:
                    for dr, dc in dirs:
                        if (r + dr, c + dc) == (r2, c2):
                            attack.add((hp2, r2, c2, j))
                    for dr, dc in dirs:
                        if valid(r2 + dr, c2 + dc):
                            if m[r2 + dr][c2 + dc] == '.':
                                in_range.add((r2 + dr, c2 + dc))
            if not attack:
                q = deque([(0, r, c)])
                reachable = set()
                seen = {(r, c)}
                while q:
                    d, rr, cc = q.popleft()
                    for dr, dc in dirs:
                        if valid(rr + dr, cc + dc):
                            if m[rr + dr][cc + dc] == '.' and (rr + dr, cc + dc) not in seen:
                                seen.add((rr + dr, cc + dc))
                                q.append((d + 1, rr + dr, cc + dc))
                                if (rr + dr, cc + dc) in in_range:
                                    reachable.add((d + 1, rr + dr, cc + dc))
                if reachable:
                    chosen = sorted(reachable)[0]
                    _, rch, cch = chosen
                    q = deque([(0, rch, cch)])
                    adj = set()
                    adj2 = {(r + dr, c + dc) for dr, dc in dirs}
                    if (rch, cch) in adj2:
                        adj = set(q)
                    seen = set()
                    while q:
                        d, rr, cc = q.popleft()
                        for dr, dc in dirs:
                            if valid(rr + dr, cc + dc):
                                if m[rr + dr][cc + dc] == '.' and (rr + dr, cc + dc) not in seen:
                                    seen.add((rr + dr, cc + dc))
                                    q.append((d + 1, rr + dr, cc + dc))
                                    if (rr + dr, cc + dc) in adj2:
                                        adj.add((d + 1, rr + dr, cc + dc))
                    if adj:
                        move_to = sorted(adj)[0][1:]
                        new_r, new_c = move_to
                        m[r][c], m[new_r][new_c] = '.', u
                        units[i][0], units[i][1] = new_r, new_c
                        r, c = new_r, new_c

                attack = set()
                for j in range(len(units)):
                    r2, c2, hp2, u2 = units[j]
                    if hp2 <= 0:
                        continue
                    if u != u2:
                        for dr, dc in dirs:
                            if (r + dr, c + dc) == (r2, c2):
                                attack.add((hp2, r2, c2, j))

            if attack:
                target = sorted(attack)[0]
                _, rt, ct, idx = target
                units[idx][2] -= {'G': 3, 'E': dmg}[u]
                if units[idx][2] <= 0:
                    m[rt][ct] = '.'

        if debug:
            draw(m, units)
            for u in sorted(units):
                if u[2] > 0:
                    print(u)
            print()

        new_units = []
        for u in units:
            if u[2] > 0:
                new_units.append(u)
        units = new_units
        rd += 1
    counter = {'G': 0, 'E': 0}
    for u in units:
        counter[u[-1]] += 1
    return [counter, (rd - 1) * sum(map(lambda x: x[2], units))]

print('Part 1:', simulate(3)[1])

dmg = 4
elves = sum(u[-1] == 'E' for u in UNITS)
while True:
    if debug:
        print('elf damage =', dmg)
    winner, s = simulate(dmg)
    if winner['E'] == elves and winner['G'] == 0:
        print('Part 2:', s)
        break
    dmg += 1