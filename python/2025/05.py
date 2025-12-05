filename = "input.txt"
data = open(filename).read().split("\n\n")
intervals = data[0].split("\n")
ingredients = list(map(int, data[1].split("\n")[:-1]))

def merge_intervals(intervals):
    inters = []
    for interval in intervals:
        l, r = list(map(int, interval.split("-")))
        inters.append([l, r])
    inters.sort()
    
    res = []
    for inter in inters:
        if len(res) == 0:
            res.append(inter)
            continue
        l, r = inter
        ll, lr = res[-1]
        if ll <= l <= lr:
            res.pop()
            res.append([ll, max(r, lr)])
        else:
            res.append(inter)
    return res

inters = merge_intervals(intervals)
res1 = 0
for ig in ingredients:
    for l, r in inters:
        if l <= ig <= r:
            res1 += 1

res2 = 0
for l, r in inters:
    res2 += r-l+1

print(res1)
print(res2)

