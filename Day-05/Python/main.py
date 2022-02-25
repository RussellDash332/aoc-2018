polymer = input()
check = [[chr(i) + chr(i + 32), chr(i + 32) + chr(i)] for i in range(65, 91)]
check = [check[i][j] for i in range(len(check)) for j in range(2)]

def react(polymer):
    found = True
    while found:
        found = False
        for s in check:
            k = polymer.find(s)
            if k != -1:
                found = True
                polymer = polymer[:k] + polymer[k+2:]
    return len(polymer)
print('Part 1:', react(polymer))
print('Part 2:', min(map(lambda x: react(polymer.replace(chr(x), '').replace(chr(x + 32), '')), range(65, 91))))