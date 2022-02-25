import sys

d, t = 0, 0
words = []
for line in sys.stdin:
    line = line.strip()
    m = {}
    for s in line:
        m[s] = m.get(s, 0) + 1
    d += int(2 in m.values())
    t += int(3 in m.values())
    words.append(line)
print('Part 1:', d * t)

def find(words):
    for word in words:
        for word2 in words:
            diff = 0
            for i in range(len(word)):
                if word[i] != word2[i]:
                    diff += 1
            if diff == 1:
                res = []
                for i in range(len(word)):
                    if word[i] == word2[i]:
                        res.append(word[i])
                return ''.join(res)
print('Part 2:', find(words))