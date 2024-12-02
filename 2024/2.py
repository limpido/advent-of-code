data = [list(map(int, line.split())) for line in open("input.txt", "r").read().splitlines()]

MIN_DIFF = 1
MAX_DIFF = 3

def is_safe(report):
    diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return all(MIN_DIFF <= d <= MAX_DIFF for d in diff) or all(-MAX_DIFF <= d <= -MIN_DIFF for d in diff)

def solve1(reports):
    return sum([is_safe(report) for report in reports])

def solve2(reports):
    return sum([any([is_safe(report[:i] + report[i+1:]) for i in range(len(report))]) for report in reports])

print(solve1(data))
print(solve2(data))
