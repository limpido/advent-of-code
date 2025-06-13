board = open("../inp.txt").read().splitlines()
board = [list(line) for line in board]
print(board)
ROW, COL = len(board), len(board[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def search(letter, r, c, visited):
    area = 1
    perimeter = 0
    visited.add((r, c))
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if (nr, nc) in visited:
            continue
        if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or board[nr][nc] != letter:
            perimeter += 1
            continue
        a, p = search(letter, nr, nc, visited)
        area += a
        perimeter += p
    board[r][c] = "*"
    return area, perimeter


price = 0
for r in range(ROW):
    for c in range(COL):
        if board[r][c] == "*":
            continue
        a, p = search(board[r][c], r, c, set())
        print(a, p, board[r][c])
        price += a * p
print(price)
