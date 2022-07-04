from email.policy import default
import sys
from collections import defaultdict

D = defaultdict(lambda: '.')
r = 0
for line in sys.stdin:
    for c in range(len(line)):
        if line[c] in '#|':
            D[(r, c)] = line[c]
    r += 1
    w = len(line.strip())

rv = []
round = 0

def do(detect=False):
    global D, round
    round += 1
    D2 = defaultdict(lambda: '.')
    for rr in range(r):
        for cc in range(w):
            adj = defaultdict(lambda: 0)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= rr + dr <= r - 1 and 0 <= cc + dc <= w - 1 and not (dr == dc == 0):
                        adj[D[(rr + dr, cc + dc)]] += 1
            if D[(rr, cc)] == '.':
                D2[(rr, cc)] = ['.', '|'][int(adj['|'] >= 3)]
            elif D[(rr, cc)] == '|':
                D2[(rr, cc)] = ['|', '#'][int(adj['#'] >= 3)]
            else:
                D2[(rr, cc)] = ['.', '#'][int(adj['|'] >= 1 and adj['#'] >= 1)]
    D = D2
    C = list(D.values())
    rv.append(C.count('#') * C.count('|'))
    if detect:
        cycle.append(C.count('#') * C.count('|'))

round = 0
for _ in range(10):
    do()
print('Part 1:', rv[-1])

# cycle manually detected starting at 415
for _ in range(405):
    do()
cycle = []
while rv[-1] not in cycle[:-1]:
    do(True)
cycle.pop()
print('Part 2:', cycle[(1000000000 - round) % len(cycle)])