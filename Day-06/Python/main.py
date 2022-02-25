import sys
maxX, maxY = 0, 0

D, D2 = {}, {}
close = [] # for part 2

checks = []
for line in sys.stdin:
    x, y = list(map(int, line.split(', ')))
    checks.append((x, y))
    maxX, maxY = max(maxX, abs(x)), max(maxY, abs(y))

for x in range(-2*maxX, 2*maxX+1):
    for y in range(-2*maxY, 2*maxY+1):
        for xc, yc in checks:
            if (x, y) not in D or abs(xc - x) + abs(yc - y) < D[(x, y)][0]:
                D[(x, y)] = [abs(xc - x) + abs(yc - y), [(xc, yc)]]
            elif abs(xc - x) + abs(yc - y) == D[(x, y)][0]:
                D[(x, y)][1].append((xc, yc))
            if x in range(-2*maxX+5, 2*maxX-4) and y in range(-2*maxY+5, 2*maxY-4):
                if (x, y) not in D2 or abs(xc - x) + abs(yc - y) < D2[(x, y)][0]:
                    D2[(x, y)] = [abs(xc - x) + abs(yc - y), [(xc, yc)]]
                elif abs(xc - x) + abs(yc - y) == D2[(x, y)][0]:
                    D2[(x, y)][1].append((xc, yc))

for x in range(-4*maxX, 4*maxX+1):
    for y in range(-4*maxY, 4*maxY+1):
        md = 0
        for xc, yc in checks:
            md += abs(x - xc) + abs(y - yc)
        if md < 10000:
            close.append((x, y))

new_D = {}
blacklist = set()
for k in D:
    if len(D[k][1]) == 1:
        if k in D2:
            if D[k][1][0] in new_D:
                new_D[D[k][1][0]].add(k)
            else:
                new_D[D[k][1][0]] = {k}
        else:
            blacklist.add(D[k][1][0])
for b in blacklist:
    del new_D[b]

print('Part 1:', max(map(len, new_D.values())))
print('Part 2:', len(close))