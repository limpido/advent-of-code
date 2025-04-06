def solve1(data):
    limit = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    res = 0
    for idx, game in enumerate(data):
        gameId = idx+1
        cubesets = game.split(':')[-1].strip().split('; ')
        possible = True
        for cubeset in cubesets:
            cubes = cubeset.split(', ')
            for cube in cubes:
                num, color = cube.split()
                if int(num) > limit[color]:
                    possible = False
                    break
            if not possible: break

        if possible: res += gameId

    return res


def solve2(data):
    res = 0

    for idx, game in enumerate(data):
        gameId = idx+1
        cubesets = game.split(':')[-1].strip().split('; ')
        nums = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for cubeset in cubesets:
            cubes = cubeset.split(', ')
            for cube in cubes:
                num, color = cube.split()
                nums[color] = max(nums[color], int(num))
        power = 1
        for n in nums.values():
            power *= n
        res += power
    return res


filename = 'input.txt'
with open(filename, 'r') as f:
    data = f.read().strip().splitlines()
    print(solve1(data))
    print(solve2(data))