import sys

M = {}
S = []
for line in sys.stdin:
    _, _, xy, wh = line.split()
    x, y = xy[:-1].split(',')
    x, y = int(x), int(y)
    w, h = wh.split('x')
    w, h = int(w), int(h)
    s = set()
    for i in range(w):
        for j in range(h):
            if (x + i, y + j) in M:
                M[(x + i, y + j)] += 1
            else:
                M[(x + i, y + j)] = 1
            s.add((x + i, y + j))
    S.append(s)

print('Part 1:', sum(map(lambda x: int(x >= 2), M.values())))
for s in range(len(S)):
    overlap = False
    for xy in S[s]:
        if M[xy] > 1:
            overlap = True
            break
    if not overlap:
        print('Part 2:', s + 1)