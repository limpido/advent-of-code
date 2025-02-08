from functools import cache

fish = list(map(int, open("input.txt").read().split(",")))

@cache
def lanternfish(timer, day=256):
    if day == 0:
        return 1
    if timer == 0:
        return lanternfish(6, day-1) + lanternfish(8, day-1)
    return lanternfish(timer-1, day-1)

print(sum(map(lanternfish, fish)))