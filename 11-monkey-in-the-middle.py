from collections import deque
from math import prod, lcm
from operator import floordiv, mod


ITEMS, OPER, TEST, A, B = range(5)


def solve(iterations, op, num):
	for _ in range(iterations):
		for idx, monkey in enumerate(monkeys):
			while monkey[ITEMS]:
				inspections[idx] += 1
				item = monkey[ITEMS].popleft()
				item = monkey[OPER](item)
				item = op(item, num)
				if item % monkey[TEST] == 0:
					monkeys[monkey[A]][ITEMS].append(item)
				else:
					monkeys[monkey[B]][ITEMS].append(item)

	inspections.sort()
	print(prod(inspections[-2:]))



with open("input.txt") as f:
	blocks = f.read().split("\n\n")

	monkeys = [
		[
			deque(map(int, item[ITEMS].replace(",", "").split()[2:])),
			eval("lambda old: " + item[OPER].split(" = ")[-1]),
			int(item[TEST].split()[-1]),
			int(item[A].split()[-1]),
			int(item[B].split()[-1])
		]
		for block in blocks for item in [block.splitlines()[1:]]
	]

	inspections = [0] * len(monkeys)


solve(20, floordiv, 3)
solve(10000, mod, lcm(*(monkey[TEST] for monkey in monkeys)))