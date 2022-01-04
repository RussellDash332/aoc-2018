import sys

v, s = set(), []
for line in sys.stdin:
    s.append(int(line))
print("Part 1:", sum(s))

c, pp = 0, 0
while c not in v:
    v.add(c)
    c += s[pp]
    pp = (pp + 1) % len(s)
print("Part 2:", c)