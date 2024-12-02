def solve1(list1, list2):
    list1.sort()
    list2.sort()
    res = 0
    for x, y in zip(list1, list2):
        res += abs(x - y)
    return res


def solve2(list1, list2):
    count = {}
    res = 0
    for n in list2:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    for n in list1:
        if n not in count:
            continue
        res += n * count[n]
    return res


filename = "../input.txt"
data = [*map(int, open(filename, "r").read().split())]
list1, list2 = sorted(data[0::2]), sorted(data[1::2])
print(solve1(list1, list2))
print(solve2(list1, list2))