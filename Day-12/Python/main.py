import sys

s = {}
for i, n in enumerate(input().split()[-1]):
    s[i] = int(n == '#')
input()
rule = {}

for line in sys.stdin:
    llcrr, n = line.strip().split(' => ')
    a, b, c, d, e = list(map(lambda x: int(x == '#'), llcrr))
    rule[16*a + 8*b + 4*c + 2*d + e] = int(n == '#')

def simulate(gen):
    ns, xs = min(s), max(s)
    state = s.copy()
    for g in range(gen):
        new_state = {}
        for i in [ns - 4, ns - 3, ns - 2, ns - 1, xs + 1, xs + 2, xs + 3, xs + 4]:
            state[i] = 0
        for pos in range(ns - 2, xs + 3):
            new_state[pos] = rule[sum([2**(4-i) * state[pos - 2 + i] for i in range(5)])]
        state = new_state
        ns -= 2
        xs += 2
        # print(g + 1, sum([k for k in state if state[k]]))
    return sum([k for k in state if state[k]])

print('Part 1:', simulate(20))
# Starting the 100ish-th generation, the sum increases by a constant
print('Part 2:', 50000000000 * (simulate(105) - simulate(104)))