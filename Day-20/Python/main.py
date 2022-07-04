import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**5)
regex = input()[1:-1]

dirs = {'W': (0, -1), 'E': (0, 1), 'N': (-1, 0), 'S': (1, 0)}

G = defaultdict(lambda: set())
pos = 0
brackets = []

def read(r=0, c=0):
    global pos, G
    base = (r, c)
    while pos < len(regex):
        curr = regex[pos]
        pos += 1
        if curr == '(':
            read(r, c)
        elif curr == '|':
            r, c = base
        elif curr == ')':
            return
        else: # NSWE
            dr, dc = dirs[curr]
            new_r, new_c = r + dr, c + dc
            G[(r, c)].add((r + dr, c + dc))
            r, c = new_r, new_c

read()
q = deque([(0, 0, 0)])
s = {(0, 0): 0}
while q:
    r, c, d = q.popleft()
    for (rr, cc) in G[(r, c)]:
        if (rr, cc) not in s:
            s[(rr, cc)] = d + 1
            q.append((rr, cc, d + 1))
print('Part 1:', max(s.values()))
print('Part 2:', len([r for r in s if s[r] >= 1000]))