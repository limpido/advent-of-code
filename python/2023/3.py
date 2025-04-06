def is_symbol(data, r, c):
    ROW, COL = len(data), len(data[0])
    if r < 0 or r >= ROW or c < 0 or c >= COL: return False
    return data[r][c] != '.' and not data[r][c].isdigit()


def solve1(data):
    ROW, COL = len(data), len(data[0])
    res = 0
    for r in range(ROW):
        cur = 0
        isPart = False
        for c in range(COL):
            if data[r][c].isdigit():
                cur = cur * 10 + int(data[r][c])
                isPart = isPart or is_symbol(data, r-1, c) or is_symbol(data, r+1, c) \
                        or is_symbol(data, r, c-1) or is_symbol(data, r, c+1) \
                        or is_symbol(data, r+1, c+1) or is_symbol(data, r-1, c+1) \
                        or is_symbol(data, r+1, c-1) or is_symbol(data, r-1, c-1)
            else:
                if cur > 0 and isPart:
                    res += cur
                cur = 0
                isPart = False
        if cur > 0 and isPart:
            res += cur
    return res


def search_num(data, r, c, nums, visited):
    ROW, COL = len(data), len(data[0])
    if r < 0 or r >= ROW or c < 0 or c >= COL or (r, c) in visited or not data[r][c].isdigit(): return (nums, visited)
    
    s = data[r][c]
    visited.add((r, c))
    
    for col in range(c+1, COL):
        if not data[r][col].isdigit():
            break
        s += data[r][col]
        visited.add((r, col))

    for col in range(c-1, -1, -1):
        if not data[r][col].isdigit():
            break
        s = data[r][col] + s
        visited.add((r, col))

    return (nums + [int(s)], visited)


def adjacent_nums(data, r, c):
    ROW, COL = len(data), len(data[0])
    nums, visited = search_num(data, r-1, c, [], set())
    nums, visited = search_num(data, r+1, c, nums, visited)
    nums, visited = search_num(data, r, c-1, nums, visited)
    nums, visited = search_num(data, r, c+1, nums, visited)
    nums, visited = search_num(data, r+1, c+1, nums, visited)
    nums, visited = search_num(data, r-1, c+1, nums, visited)
    nums, visited = search_num(data, r+1, c-1, nums, visited)
    nums, visited = search_num(data, r-1, c-1, nums, visited)
    return nums


def solve2(data):
    ROW, COL = len(data), len(data[0])
    GEAR = '*'
    res = 0

    for r in range(ROW):
        for c in range(COL):
            if data[r][c] == GEAR:
                adjacentNums = adjacent_nums(data, r, c)
                if len(adjacentNums) == 2:
                    res += adjacentNums[0] * adjacentNums[1]
    return res


filename = 'input.txt'
with open(filename, 'r') as f:
    data = f.read().strip().splitlines()
    print(solve1(data))
    print(solve2(data))