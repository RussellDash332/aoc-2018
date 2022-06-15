import sys
import time as tim
from heapq import *

rule = {}
rev = {}
for line in sys.stdin:
    line = line.split()
    a, b = line[1], line[7]
    for tree in [rule, rev]:
        tree[a] = tree.get(a, []) + [b]
        tree[b] = tree.get(b, [])
        a, b = b, a

def simulate():
    done = set()
    q = sorted(i for i in rev if not rev[i])
    p = []
    while q:
        v = heappop(q)
        p.append(v)
        done.add(v)
        for n in rule[v]:
            if all(map(lambda x: x in done, rev[n])):
                heappush(q, n)
    return ''.join(p)

def simulate2(workers):
    tasks = [None] * workers
    done = set()
    q = list(rev.keys())
    time = 0

    while len(done) != len(rule):
        for _ in range(workers + 1):
            v = None
            if q:
                for n in q:
                    if all(map(lambda x: x in done, rev[n])):
                        v = n
                        q.remove(v)
                        break
            found = False
            for i in range(workers):
                if tasks[i] == None:
                    if v != None:
                        tasks[i] = (v, time + ord(v) - ord('A') + 60 + 1)
                        found = True
                        break
                elif tasks[i][1] == time:
                    done.add(tasks[i][0])
                    tasks[i] = None
            if v != None and not found:
                q.append(v)
                q.sort()
        time += 1
    return time - 1

print('Part 1:', simulate())
print('Part 2:', simulate2(5))