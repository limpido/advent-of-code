def strategy1():
	score = 0
	win = {
		'X': 'C',
		'Y': 'A',
		'Z': 'B'
	}

	lose = {
		'X': 'B',
		'Y': 'C',
		'Z': 'A'
	}

	shape = {
		'X': 1,
		'Y': 2,
		'Z': 3
	}

	with open("input.txt") as file:
		for line in file.readlines():
			op, me = line[:-1].split(' ')
			score += shape[me]
			if op == win[me]:
				score += 6
			elif op != lose[me]:
				score += 3
	print(score)

def strategy2():
	score = 0

	win = {
		'A': 'B',
		'B': 'C',
		'C': 'A'
	}

	lose = {
		'A': 'C',
		'B': 'A',
		'C': 'B'
	}

	shape = {
		'A': 1,
		'B': 2,
		'C': 3
	}

	with open("input.txt") as file:
		for line in file.readlines():
			op, res = line[:-1].split(' ')
			if res == 'X':  # lose
				score += shape[lose[op]]
			elif res == 'Y': # draw
				score += 3
				score += shape[op]
			else: # win
				score += 6
				score += shape[win[op]]
	print(score)

