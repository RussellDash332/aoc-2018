import sys
from datetime import datetime

schedule = []
for line in sys.stdin:
    schedule.append(line.strip())
schedule.sort()

log = {}
log2 = {}
base = datetime(1518, 2, 27, 23, 0)
for s in schedule:
    time = datetime.strptime(s[1:s.find(']')], '%Y-%m-%d %H:%M')
    event = s[s.find(']')+2:]
    if event.startswith('Guard'):
        guard = int(event.split()[1][1:])
    elif event == 'falls asleep':
        start = time
    else:
        log[guard] = log.get(guard, {})
        for m in range(int((start - base).total_seconds()) // 60, int((time - base).total_seconds()) // 60):
            log[guard][m % 60] = log[guard].get(m % 60, 0) + 1
            log2[m % 60] = log2.get(m % 60, {})
            log2[m % 60][guard] = log2[m % 60].get(guard, 0) + 1

best_guard = max(log, key=lambda x: (sum(log[x].values()), x))
best_min = max(log[best_guard], key=lambda x: (log[best_guard][x], x))
print('Part 1:', best_guard * best_min)

best_min2 = max(log2, key=lambda x: max(log2[x].values()))
print('Part 2:', best_min2 * max(log2[best_min2], key=lambda x: log2[best_min2][x]))