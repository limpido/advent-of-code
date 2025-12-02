filename = "input.txt"
data = open(filename, "r").readline()[:-1].split(",")

def is_repeated_pattern(s):
    return s in (s+s)[1:-1]

res1 = 0
res2 = 0
for d in data:
    start, end = map(int, d.split("-"))
    for n in range(start, end+1):
        if is_repeated_pattern(str(n)):
            res2 += n
        l = len(str(n))
        if str(n)[:l//2] == str(n)[l//2:]:
            res1 += n
print(res1)
print(res2)
