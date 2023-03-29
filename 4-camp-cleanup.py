def contain():
	count = 0
	with open("input.txt") as file:
		for line in file.readlines():
			first, second = line[:-1].split(',')
			left1, right1 = [int(s) for s in first.split('-')]
			left2, right2 = [int(s) for s in second.split('-')]
			if left1 <= left2 and right1 >= right2 or left2 <= left1 and right2 >= right1:
				count += 1
	print(count)


def overlap():
	count = 0
	with open("input.txt") as file:
		for line in file.readlines():
			first, second = line[:-1].split(',')
			left1, right1 = [int(s) for s in first.split('-')]
			left2, right2 = [int(s) for s in second.split('-')]
			if left1 <= left2 <= right1 or left2 <= left1 <= right2:
				count += 1
	print(count)

