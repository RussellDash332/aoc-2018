recipes = input()
board = ["3", "7"]
e1, e2 = 0, 1

while len(board) <= int(recipes) + 10:
    new = int(board[e1]) + int(board[e2])
    board.extend(str(new))
    e1 = (e1 + int(board[e1]) + 1) % len(board)
    e2 = (e2 + int(board[e2]) + 1) % len(board)
print(f"Part 1: {''.join(board[int(recipes):int(recipes)+10])}")

board = ["3", "7"]
e1, e2 = 0, 1
# Could have one extra digit
while recipes not in ''.join(board[-len(recipes)-1:]):
    new = int(board[e1]) + int(board[e2])
    board.extend(str(new))
    e1 = (e1 + int(board[e1]) + 1) % len(board)
    e2 = (e2 + int(board[e2]) + 1) % len(board)
print(f"Part 2: {len(board) - len(recipes) - int(board[-1] != recipes[-1])}")