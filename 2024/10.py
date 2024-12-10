board = [list(map(int,r)) for r in open("input.txt").read().splitlines()]
ROW, COL = len(board), len(board[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(r, c, target, visited):
    if r < 0 or r >= ROW or c < 0 or c >= COL:
        return 0
    if board[r][c] != target:
        return 0
    if target == 9:
        seen = (r, c) in visited
        visited.add((r, c))
        return 0 if part == 1 and seen else 1
    return sum([dfs(r + dr, c + dc, target + 1, visited) for dr, dc in directions])

for part in [1, 2]:
    print(sum([dfs(r, c, 0, set()) for r in range(ROW) for c in range(COL) if board[r][c] == 0]))