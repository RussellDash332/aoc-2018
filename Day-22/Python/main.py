import sys
sys.setrecursionlimit(50000)

depth = int(input().split()[-1])
tx, ty = map(int, input().split()[-1].split(','))
XMAX, YMAX = 5*tx, 5*ty # big enough
gi, el, m = {}, {}, {}

for x in range(XMAX + 1):
    gi[(x, 0)] = x * 16807
    el[(x, 0)] = (gi[(x, 0)] + depth) % 20183
for y in range(YMAX + 1):
    gi[(0, y)] = y * 48271
    el[(0, y)] = (gi[(0, y)] + depth) % 20183
for x in range(1, XMAX + 1):
    for y in range(1, YMAX + 1):
        if (tx, ty) == (x, y):
            gi[(x, y)] = 0
        else:
            gi[(x, y)] = el[(x - 1, y)] * el[(x, y - 1)]
        el[(x, y)] = (gi[(x, y)] + depth) % 20183
for x, y in el:
    el[(x, y)] %= 3
    m[(x, y)] = '.=|'[el[(x, y)]]
m[(0, 0)] = 'M'
m[(tx, ty)] = 'T'

def draw():
    for y in range(YMAX + 1):
        for x in range(XMAX + 1):
            print(m[(x, y)],end='')
        print()
    print()
#draw()

s = 0
for y in range(ty + 1):
    for x in range(tx + 1):
        s += el[(x, y)]
print('Part 1:', s)

from heapq import *
d = {}
q = [(0, 0, 0, 'torch')]
legal_el = {
    'torch': [0, 2],
    'climb': [0, 1],
    'neither': [1, 2]
}
import time
while q:
    t, x, y, eq = heappop(q)
    if (x, y, eq) in d and d[(x, y, eq)] < t:
        continue
    if (x, y, eq) == (tx, ty, 'torch'):
        break
    for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        if el[(x, y)] in legal_el[eq] and (x + dx, y + dy) in el:
            # Move?
            if el[(x + dx, y + dy)] in legal_el[eq]:
                if (x + dx, y + dy, eq) in d and d[(x + dx, y + dy, eq)] < t + 1:
                    continue
                d[(x + dx, y + dy, eq)] = t + 1
                if (t + 1, x + dx, y + dy, eq) in q:
                    continue
                heappush(q, (t + 1, x + dx, y + dy, eq))
    # Change gears?
    for e in legal_el:
        if el[(x, y)] in legal_el[e] and e != eq:
            e2 = e
            break
    if (x, y, e2) in d and d[(x, y, e2)] < t + 7:
        continue
    d[(x, y, e2)] = t + 7
    if (t + 7, x, y, e2) in q:
        continue
    heappush(q, (t + 7, x, y, e2))
print('Part 2:', d[(tx, ty, 'torch')])

'''
def torch(x, y, t):
    if (x, y) not in d:
        d[(x, y)] = t
    else:
        d[(x, y)] = min(t, d[(x, y)])
    if (x, y) == (tx, ty):
        return
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if (x + dx, y + dy) in el:
            if el[(x + dx, y + dy)] in [0, 2]:
                torch(x + dx, y + dy, t + 1)
    if el[(x, y)] == 0:
        climb(x, y, t + 7)
    elif el[(x, y)] == 2:
        neither(x, y, t + 7)

def climb(x, y, t):
    if (x, y) not in d:
        d[(x, y)] = t
    else:
        d[(x, y)] = min(t, d[(x, y)])
    if (x, y) == (tx, ty):
        return
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if (x + dx, y + dy) in el:
            if el[(x + dx, y + dy)] in [0, 1]:
                climb(x + dx, y + dy, t + 1)
    if el[(x, y)] == 0:
        torch(x, y, t + 7)
    elif el[(x, y)] == 1:
        neither(x, y, t + 7)

def neither(x, y, t):
    if (x, y) not in d:
        d[(x, y)] = t
    else:
        d[(x, y)] = min(t, d[(x, y)])
    if (x, y) == (tx, ty):
        return
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if (x + dx, y + dy) in el:
            if el[(x + dx, y + dy)] in [1, 2]:
                neither(x + dx, y + dy, t + 1)
    if el[(x, y)] == 1:
        climb(x, y, t + 7)
    elif el[(x, y)] == 2:
        torch(x, y, t + 7)
'''