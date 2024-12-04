board = open("input.txt").read().strip().splitlines()
ROW, COL = len(board), len(board[0])


def dfs(r, c, dr, dc, target):
    if r < 0 or r >= ROW or c < 0 or c >= COL:
        return 0
    if board[r][c] != target[0]:
        return 0
    if len(target) == 1:
        return 1
    return dfs(r + dr, c + dc, dr, dc, target[1:])


def part1():
    target = "XMAS"
    diff = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    res = 0
    for r in range(ROW):
        for c in range(COL):
            for dr, dc in diff:
                res += dfs(r, c, dr, dc, target)
    print(res)


def part2():
    diff = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    res = 0
    for r in range(1, ROW - 1):
        for c in range(1, COL - 1):
            if board[r][c] == "A":
                if (
                    [set(board[r + dr][c + dc] for (dr, dc) in diff)][0]
                    == set(["M", "S"])
                    and board[r + 1][c + 1] != board[r - 1][c - 1]
                    and board[r + 1][c - 1] != board[r - 1][c + 1]
                ):
                    res += 1
    print(res)


# part 2 method 2, reuse dfs utility
def part22():
    target = ["MAS", "SAM"]
    res = 0
    for r in range(ROW):
        for c in range(COL):
            if any(dfs(r, c, 1, 1, t) for t in target):
                if any(dfs(r, c + 2, 1, -1, t) for t in target):
                    res += 1
    print(res)


part1()
part2()
part22()


targets = ["MMSS", "MSSM", "SSMM", "SMMS"]
