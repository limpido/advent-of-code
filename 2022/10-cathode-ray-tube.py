def solver():
	total = 0
	strengths = [0]

	with open("input.txt") as f:
		lines = f.readlines()
		x = 1
		for line in lines:
			if line[:-1] == 'noop':
				strengths.append(x)
			else:
				ins, num = line[:-1].split()
				num = int(num)
				strengths.extend([x, x])
				x += num

	for i in range(20, 221, 40):
		total += i * strengths[i]
			
	print(total)

solver()


def draw_helper(cur, x, row, pixels):
	if x-1 <= cur <= x+1:
		row += '#'
	else:
		row += '.'
	cur += 1
	
	if cur > 0 and cur % 40 == 0:
		pixels.append(row[:])
		row = ''
		cur = 0

	return cur, row, pixels



def draw_CRT():
	pixels = []
	x = 1
	with open("input.txt") as f:
		lines = f.readlines()
		row = ''
		cur = 0
		for i in range(len(lines)):
			line = lines[i]
			
			if line[:-1] == 'noop':
				cur, row, pixels = draw_helper(cur, x, row, pixels)
			else:
				ins, num = line[:-1].split()
				num = int(num)
				cur, row, pixels = draw_helper(cur, x, row, pixels)
				cur, row, pixels = draw_helper(cur, x, row, pixels)
				x += num

	print(pixels)


draw_CRT()