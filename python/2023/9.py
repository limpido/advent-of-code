data = [line.split() for line in open("in.txt").readlines()]
data = [list(map(int, arr)) for arr in data]


def get_extrapolated_value(data):
    lines = [data]
    while True:
        diff = []
        cur_line = lines[-1]
        for i in range(1, len(cur_line)):
            diff.append(cur_line[i] - cur_line[i - 1])
        if not any(diff):
            break
        lines.append(diff)

    val1 = val2 = 0
    for i in range(len(lines) - 1, -1, -1):
        val1 += lines[i][-1]
        val2 = lines[i][0] - val2
    return val1, val2


total1 = total2 = 0
for d in data:
    v1, v2 = get_extrapolated_value(d)
    total1 += v1
    total2 += v2
print(total1, total2)
