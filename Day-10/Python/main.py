import sys, re

stars = []
for line in sys.stdin:
    stars.append(list(map(int, re.findall('position=<([-\s\d]+),([-\s\d]+)> velocity=<([-\s\d]+),([-\s\d]+)>', line.strip())[0])))

def draw(xlim, ylim):
    x1 = min(map(lambda x: x[0], stars))
    x2 = max(map(lambda x: x[0], stars)) + 1
    y1 = min(map(lambda x: x[1], stars))
    y2 = max(map(lambda x: x[1], stars)) + 1
    m = []
    if xlim >= x2 - x1 and ylim >= y2 - y1:
        for _ in range(y2 - y1):
            m.append(['.'] * (x2 - x1))
        for x, y, *_ in stars:
            m[y - y1][x - x1] = '#'
        for r in m:
            print(''.join(r))
        return True
    else:
        print(f'Map size: {x2 - x1}x{y2 - y1}')
        return False

for d in range(10370):
    print(f'Day {d}:')
    if not draw(150, 150):
        print('Map too big')
    for i in range(len(stars)):
        stars[i][0] += stars[i][2]
        stars[i][1] += stars[i][3]
    print()