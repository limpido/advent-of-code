filename = "input.txt"
banks = open(filename).read().split()
banks = [[int(d) for d in b] for b in banks]

def largest(arr, start, end):
    res = 0
    idx = 0
    for i, n in enumerate(arr):
        if i < start: continue
        if i >= end: break
        if n > res:
            res = n
            idx = i
    return res, idx

def largest_n_digit(arr, n_digit):
    res = 0
    start = 0
    for nth in range(n_digit):
        end = len(arr) - (n_digit - nth - 1)
        n, i = largest(arr, start, end)
        start = i+1
        res = res * 10 + n
    return res


res1, res2 = 0, 0
for bank in banks:
    res1 += largest_n_digit(bank, 2)
    res2 += largest_n_digit(bank, 12)
print(res1, res2)
