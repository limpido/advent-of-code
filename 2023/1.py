def solve1(data):
    res = 0
    for line in data:
        nums = []
        for c in line:
            if '0' <= c <= '9':
                nums.append(c)
        res += int(nums[0]) * 10 + int(nums[-1])
    return res


def search(s, target):
    for i, c in enumerate(target):
        if i >= len(s) or s[i] != c:
            return False
    return True


def solve2(data):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    res = 0
    for line in data:
        nums = []
        for i, c in enumerate(line):
            if '0' <= c <= '9':
                nums.append(c)
                continue
            for j, digit in enumerate(digits):
                if search(line[i:], digit):
                    nums.append(j+1)
                    break
        res += int(nums[0]) * 10 + int(nums[-1])

    return res


filename = '../input.txt'
with open(filename, 'r') as f:
    data = f.read().strip().splitlines()
    print(solve1(data))
    print(solve2(data))