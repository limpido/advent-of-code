def count_largest():
	largest = 0
	cur = 0
	with open("input.txt") as file:
		for line in file.readlines():
			if line == '\n':
				largest = max(largest, cur)
				cur = 0
			else:
				num = int(line[:-1])
				cur += num
	print(largest)


def count_top_3():
	top = []
	stack = []
	cur = 0
	with open("input.txt") as file:
		for line in file.readlines():
			if line == '\n':
				print(cur, len(top))
				while len(top) and cur > top[-1]:
					stack.append(top.pop())
				if len(top) < 3:
					top.append(cur)
				while len(stack) and len(top) < 3:
					top.append(stack.pop())
				print(top)
				cur = 0
			else:
				cur += int(line[:-1])
	print(top, sum(top))