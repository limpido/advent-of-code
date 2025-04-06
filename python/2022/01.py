calories = [sum(map(int, line.split())) for line in open("input.txt").read().split("\n\n")]
print(max(calories))
print(sum(sorted(calories)[-3:]))