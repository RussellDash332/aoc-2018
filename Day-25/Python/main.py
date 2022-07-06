import sys

coords = []
for line in sys.stdin:
    coords.append(list(map(int, line.split(','))))

def manhattan(c1, c2):
    return sum(abs(a - b) for a, b in zip(c1, c2))

const = [[coords[0]]]
coords.pop(0)
while coords:
    added = False
    new_coords = []
    for i in range(len(coords)):
        found = False
        for j in range(len(const[-1])):
            if manhattan(const[-1][j], coords[i]) <= 3:
                const[-1].append(coords[i])
                added = True
                found = True
                break
        if not found:
            new_coords.append(coords[i])
    if not added:
        const.append([new_coords.pop()])
    coords = new_coords
print('Part 1:', len(const))
print('Part 2: THE END!')