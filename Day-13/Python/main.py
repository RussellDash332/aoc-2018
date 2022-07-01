import sys
from copy import deepcopy

debug = False

m = []
for line in sys.stdin:
    m.append(list(line.strip('\n\r')))

minecarts = []
d = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
t = {
    0: (lambda r, c: (c, r) if r else (-c, -r)),
    2: (lambda r, c: (c, r) if c else (-c, -r)),
    1: (lambda r, c: (r, c))
}
# Works since no minecart were initially on a curve or intersection
p = {'<': '-', '>': '-', '^': '|', 'v': '|'}
for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] in '<>^v':
            dr, dc = d[m[r][c]]
            m[r][c] = p[m[r][c]]
            minecarts.append([r, c, dr, dc, 0])
minecarts2 = deepcopy(minecarts)

def draw():
    m2 = deepcopy(m)
    for r, c, *_ in minecarts:
        m2[r][c] = '\033[91m#\033[0m'
    ret = []
    for r in m2:
        ret.append(''.join(r))
    print('\n'.join(ret))

crash = False
cx, cy = None, None
while not crash:
    seen, crash = set(), False
    minecarts.sort(key=lambda x: x[:2])
    for minecart in minecarts:
        minecart[0] += minecart[2]
        minecart[1] += minecart[3]
        r, c, dr, dc, mt = minecart
        if m[r][c] == '\\':
            minecart[2], minecart[3] = dc, dr
        elif m[r][c] == '/':
            minecart[2], minecart[3] = -dc, -dr
        elif m[r][c] == '+':
            minecart[2], minecart[3] = t[mt](dr, dc)
            minecart[4] = (mt + 1) % 3
        if tuple(minecart[:2]) in seen:
            crash, cx, cy = True, minecart[1], minecart[0]
        seen.add(tuple(minecart[:2]))
    if debug:
        for mc in sorted(minecarts):
            print(mc)
        draw()
print('Part 1:', f'{cx},{cy}')

minecarts = minecarts2
while len(minecarts) != 1:
    new_minecarts = []
    crash = set()
    minecarts.sort(key=lambda x: x[:2])
    for i, minecart in enumerate(minecarts):
        minecart[0] += minecart[2]
        minecart[1] += minecart[3]
        r, c, dr, dc, mt = minecart
        if m[r][c] == '\\':
            minecart[2], minecart[3] = dc, dr
        elif m[r][c] == '/':
            minecart[2], minecart[3] = -dc, -dr
        elif m[r][c] == '+':
            minecart[2], minecart[3] = t[mt](dr, dc)
            minecart[4] = (mt + 1) % 3
        for i2, minecart2 in enumerate(minecarts):
            if i != i2 and minecart[:2] == minecart2[:2]:
                crash |= {i, i2}
    for i in range(len(minecarts)):
        if i not in crash:
            new_minecarts.append(minecarts[i])
    minecarts = new_minecarts
    if debug:
        for mc in sorted(minecarts):
            print(mc)
        draw()
print('Part 2:', f'{minecarts[0][1]},{minecarts[0][0]}')