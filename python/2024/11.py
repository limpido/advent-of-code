from functools import cache

stones = list(map(int, open("input.txt").read().split(" ")))

# functools.cache creates a thin wrapper around a dictionary lookup for the function arguments
@cache
def get_num_of_stone(stone, blinks=75):
    if blinks == 0:
        return 1
    if stone == 0:
        return get_num_of_stone(1, blinks-1)
    if len(str(stone)) % 2 == 0:
        size = len(str(stone))
        stone1, stone2 = int(stone // (10 ** (size // 2))), int(stone % (10 ** (size // 2)))
        return get_num_of_stone(stone1, blinks-1) + get_num_of_stone(stone2, blinks-1)
    return get_num_of_stone(stone * 2024, blinks - 1)

print(sum(map(get_num_of_stone, stones)))


# cache without using functools.cache
cache = {}
def get_num_of_stone2(stone, blinks=75):
    if blinks == 0:
        return 1
    if (stone, blinks) in cache:
        return cache[(stone, blinks)]
    if stone == 0:
        val = get_num_of_stone(1, blinks-1)
    elif len(str(stone)) % 2 == 0:
        size = len(str(stone))
        stone1, stone2 = int(stone // (10 ** (size // 2))), int(stone % (10 ** (size // 2)))
        val = get_num_of_stone(stone1, blinks-1) + get_num_of_stone(stone2, blinks-1)
    else:
        val = get_num_of_stone(stone * 2024, blinks - 1)
    cache[(stone, blinks)] = val
    return val

print(sum(map(get_num_of_stone2, stones)))
