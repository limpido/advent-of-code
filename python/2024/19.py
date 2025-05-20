a, b = open("in.txt").read().split("\n\n")
patterns = a.split(", ")
targets = b.splitlines()


## Method 1
from functools import cache


@cache
def is_possible(target, op):
    return not target or op(
        is_possible(target[len(p) :], op) for p in patterns if target.startswith(p)
    )


for op in any, sum:
    print(sum(is_possible(target, op) for target in targets))


## Method 2
cache = {}


def ways(patterns, target):
    if target in cache:
        return cache[target]
    ans = 0
    if not target:
        ans = 1
    for p in patterns:
        if target.startswith(p):
            ans += ways(patterns, target[len(p) :])
    cache[target] = ans
    return ans


p1 = p2 = 0

for target in targets:
    target_ways = ways(patterns, target)
    if target_ways > 0:
        p1 += 1
    p2 += target_ways

print(p1, p2)
