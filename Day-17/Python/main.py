import sys
from collections import deque

sys.setrecursionlimit(10**5)
SOURCE = (500, 0)
C, F, S = set(), set(), set()
q = deque([])

xmin, xmax, ymin, ymax = SOURCE[0], SOURCE[0], float('inf'), -float('inf')
for line in sys.stdin:
    fixed, ranged = line.strip().split(', ')
    axis_fixed, fixed = fixed.split('=')
    fixed = int(fixed)
    axis_ranged, ranged = ranged.split('=')
    ranged_start, ranged_end = map(int, ranged.split('..'))
    if axis_fixed == 'x':
        xmin = min(xmin, fixed)
        xmax = max(xmax, fixed)
        ymin = min(ymin, ranged_start)
        ymax = max(ymax, ranged_end)
        for y in range(ranged_start, ranged_end + 1):
            C.add((fixed, y))
    else:
        ymin = min(ymin, fixed)
        ymax = max(ymax, fixed)
        xmin = min(xmin, ranged_start)
        xmax = max(xmax, ranged_end)
        for x in range(ranged_start, ranged_end + 1):
            C.add((x, fixed))

def draw(xh=None, yh=None):
    m = []
    for y in range(ymin, ymax + 1):
        m.append(['.'] * (xmax - xmin + 1))
    for x, y in C:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            m[y - ymin][x - xmin] = '#'
    for x, y in F:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            m[y - ymin][x - xmin] = '|'
    for x, y in S:
        if xmin <= x <= xmax and ymin <= y <= ymax:
            m[y - ymin][x - xmin] = '~'
    if (xh, yh) != (None, None): # highlight, for debugging
        s = m[yh - ymin][xh - xmin]
        m[yh - ymin][xh - xmin] = f'\033[91m{s[5]}\033[0m'
    m[SOURCE[1] - ymin][SOURCE[0] - xmin] = '+'
    with open('../frame.txt', 'w+') as f:
        f.write('\n'.join(map(lambda x: ''.join(x), m)))

# buffer
xmin -= 3
xmax += 3

def fill(x, y, dx, dy):
    # add to flowing spots
    F.add((x, y))
    
    # if empty space and haven't been flowed by water, recurse
    if (x, y + 1) not in C and (x, y + 1) not in F and SOURCE[1] <= y <= ymax:
        fill(x, y + 1, 0, 1)
    
    # water is not settled
    if (x, y + 1) not in C and (x, y + 1) not in S:
        return False

    # keep filling to the left and right recursively until hit a clay
    lf = (x - 1, y) in C or ((x - 1, y) not in F and fill(x - 1, y, -1, 0))
    rf = (x + 1, y) in C or ((x + 1, y) not in F and fill(x + 1, y, 1, 0))

    # add the seemingly settled spots to the set
    d, e = -1, 1
    if (dx, dy) == (0, 1) and all([lf, rf]):
        S.add((x, y))
        while (x + d, y) in F:
            S.add((x + d, y))
            d -= 1
        while (x + e, y) in F:
            S.add((x + e, y))
            e += 1

    # water is settled
    return ((dx, dy) == (-1, 0) and (lf or (x + d, y) in C)) or ((dx, dy) == (1, 0) and (rf or (x + e, y) in C))

fill(*SOURCE, 0, 1)
F = set(filter(lambda p: ymin <= p[1] <= ymax, F))
S = set(filter(lambda p: ymin <= p[1] <= ymax, S))
draw()
print('Part 1:', len(F))
print('Part 2:', len(S))