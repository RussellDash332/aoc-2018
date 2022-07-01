sn = int(input())
pll = {}

def pl(x, y):
    return ((x + 10)**2 * y + (x + 10) * sn) % 1000 // 100 - 5

pll = []
for i in range(301):
    pll.append([0] * 301)
for i in range(1, 301):
    cs = 0
    for j in range(1, 301):
        cs += pl(i, j)
        pll[i][j] = pll[i - 1][j] + cs

# No time to DP ;)
def spl(x0, y0, size=3):
    return pll[x0 + size - 1][y0 + size - 1] - pll[x0 + size - 1][y0 - 1] - pll[x0 - 1][y0 + size - 1] + pll[x0 - 1][y0 - 1]

bx, by, bs = 1, 1, float('-inf')
for x in range(1, 298):
    for y in range(1, 298):
        s = spl(x, y)
        if s > bs:
            bx, by, bs = x, y, s
print(f'Part 1: {bx},{by}')

bz = 3
for z in range(1, 301):
    if z == 3:
        continue
    for x in range(1, 301 - z):
        for y in range(1, 301 - z):
            s = spl(x, y, z)
            if s > bs:
                bx, by, bs, bz = x, y, s, z
print(f'Part 2: {bx},{by},{bz}')