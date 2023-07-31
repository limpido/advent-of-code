def find_misplaced():
	res = 0
	with open("input.txt") as file:
		for items in file.readlines():
			l = len(items) // 2
			part1, part2 = items[:l], items[l:-1]
			s = set(part1)
			for item in part2:
				if item in s:
					res += priority(item)
					break

	print(res)


def priority(item):
	if item.isupper():
		return ord(item)-ord('A')+27
	else:
		return ord(item)-ord('a')+1


def badge():
	res = 0
	with open("input.txt") as file:
		lines = file.readlines()
		for i in range(0, len(lines), 3):
			a, b, c = [s[:-1] for s in lines[i:i+3]]
			common = set(a) & set(b) & set(c)
			for item in common:
				res += priority(item)
	print(res)

