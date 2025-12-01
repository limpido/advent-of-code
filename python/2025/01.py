filename = "input.txt"
data = open(filename, "r").read().splitlines()

def part1():
    count = 0
    cur = 50
    for d in data:
        offset = int(d[1:])
        if d[0] == 'L':
            cur -= offset
        else:
            cur += offset
        cur %= 100
        if cur == 0:
            count += 1
    print(count)

def part2():
    count = 0
    cur = 50
    for d in data:
        offset = int(d[1:])
        if d[0] == 'L':
            for i in range(offset):
                cur += 1
                cur %= 100
                if cur == 0:
                    count += 1
        else:
            for i in range(offset):
                cur -= 1
                cur %= 100
                if cur == 0:
                    count += 1
    print(count)

part1()
part2()
