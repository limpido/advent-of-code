lines = open("../inp.txt").read().splitlines()
robots = set()
for l in lines:
    p, v = map(lambda a: tuple(map(int, a.split("=")[1].split(","))), l.split(" "))
    robots.add((p, v))

ROW, COL = 103, 101
positions = {}


def pos(p, v, t):
    px, py = p
    vx, vy = v
    px = (px + vx * t) % COL
    py = (py + vy * t) % ROW
    return (px, py)


for p, v in robots:
    np = pos(p, v, 100)
    if np in positions:
        positions[np] += 1
    else:
        positions[np] = 1


def count(X, Y):
    x1, x2 = X
    y1, y2 = Y
    res = 0
    for p, n in positions.items():
        x, y = p
        if x1 <= x <= x2 and y1 <= y <= y2:
            res += n
    return res


res = 1
for y in ((0, ROW // 2 - 1), (ROW // 2 + 1, ROW - 1)):
    for x in ((0, COL // 2 - 1), (COL // 2 + 1, COL - 1)):
        res *= count(x, y)
print(res)
