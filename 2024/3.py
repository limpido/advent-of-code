import re
from operator import mul

data = open("input.txt").read().strip()


# part 1
expr = re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", data)
print(sum(list(map(eval, expr))))


# part 2
res = 0
start, end = 0, -1
do = re.search(r"do\(\)", data[start:])
dont = re.search(r"don\'t\(\)", data[start:])
if do:
    end = do.start()
if dont:
    end = min(end, dont.start())
res += sum(list(map(eval, re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", data[:end]))))
start = end

while 0 < start <= len(data):
    do = re.search(r"do\(\)", data[start:])
    if do is None:
        break
    dont = re.search(r"don\'t\(\)", data[start+do.end():])
    end = -1 if dont is None else start + do.end() + dont.start()
    res += sum(list(map(eval, re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", data[start+do.end():end]))))
    start = end
print(res)


# part 2 method 2
data = "".join(part.split("don't()")[0] for part in data.split("do()"))
res = sum(list(map(eval, re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", data))))
print(res)