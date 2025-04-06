def solve(time, dist):
    res = 1
    for (t, target) in zip(time, dist):
        ways = 0
        for speed in range(1, t):
            d = speed * (t-speed)
            if d > target:
                ways += 1
        res *= ways
    return res


filename = '../input.txt'
with open(filename, 'r') as f:
    time, distance = f.read().strip().splitlines()

    # part 1
    time1 = [int(t) for t in time.split(":")[1].strip().split()]
    distance1 = [int(d) for d in distance.split(":")[1].strip().split()]
    print(solve1(time1, distance1))
    
    # part 2
    time2 = "".join(time.split(":")[1].split())
    distance2 = "".join(distance.split(":")[1].split())
    print(solve([int(time2)], [int(distance2)]))