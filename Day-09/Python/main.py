s = input().split()
players, last = int(s[0]), int(s[-2])

class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class CLL:
    def __init__(self):
        self.tail = None
        self.size = 0

    def insert_at(self, node, at):
        prev, curr, succ = at, node, at.next
        prev.next, curr.prev, curr.next, succ.prev = curr, prev, succ, curr
        if self.tail == prev:
            self.tail = curr
        self.size += 1

def simulate(last):
    marbles = CLL()
    pos = Node(0)
    pos.next, pos.prev = pos, pos
    marbles.tail, marbles.size = pos, 1
    marbs = 1
    score = {}

    while marbs <= last:
        ply = marbs % players
        if marbs % 23 != 0:
            pos = pos.next
            marbles.insert_at(Node(marbs), pos)
            pos = pos.next
        else:
            for _ in range(7):
                pos = pos.prev
            score[ply] = score.get(ply, 0) + pos.val + marbs
            pos.prev.next, pos.next.prev, pos = pos.next, pos.prev, pos.next
            marbles.size -= 1
        marbs += 1
    return max(score.values())

print('Part 1:', simulate(last))
print('Part 2:', simulate(100 * last))