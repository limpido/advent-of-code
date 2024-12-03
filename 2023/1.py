import re

data = open("input.txt").read().strip().splitlines()

# part 1
res = sum(int(d[0] + d[-1]) for d in [re.findall(r"\d", line) for line in data])
print(res)


# part 2
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_pattern = re.compile(r"(?=(\d|" + "|".join(digits) + "))")

def word2digit(s):
    return str(digits.index(s)+1) if len(s) > 1 else s

res = sum(int("".join(map(word2digit, (d[0], d[-1])))) for d in [digit_pattern.findall(line) for line in data])
print(res)
