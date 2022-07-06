import re, sys

nanobots = []
for line in sys.stdin:
    line = re.findall('pos=<([-\d]+),([-\d]+),([-\d]+)>, r=(\d+)', line.strip())[0]
    nanobots.append(list(map(int, line)))
strongest = max(nanobots, key=lambda x: x[-1])

def contained(nanobot, container):
    x, y, z, _ = nanobot
    xs, ys, zs, rs = container
    return abs(xs - x) + abs(ys - y) + abs(zs - z) <= rs
print('Part 1:', sum(contained(n, strongest) for n in nanobots))

q = []
# Treat the MD as a sliding window, we add the bots by +1 or -1, get the point at the maximum bot count
for x, y, z, r in nanobots:
    d = abs(x) + abs(y) + abs(z)
    # Bot in range from MD of max(0, d - r) to d + r
    q.extend([(max(0, d - r), 1), (d + r, -1)])
c, mc, md = 0, 0, 0
for pos, inc in sorted(q):
    c += inc
    if c > mc:
        mc, md = c, pos
print('Part 2:', md)