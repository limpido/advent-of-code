'''
consider 3 cases:
1. head and tail in the same row/col
2. head above tail / head is on the left
3. head below tail / head is on the right
'''


def solve():
	with open("input.txt") as f:
		rh, ch = 0, 0
		rt, ct = 0, 0
		visited = set()

		lines = f.read().strip().splitlines()
		
		for line in lines:
			direction, step = line.split(' ')
			step = int(step)

			match direction:
				case 'L':
					for _ in range(step):
						if ch < ct:
							rt = rh
							ct = ch
						ch -= 1
						visited.add((rt, ct))
				case 'R':
					for _ in range(step):
						if ch > ct:
							rt = rh
							ct = ch
						ch += 1
						visited.add((rt, ct))
				case 'U':
					for _ in range(step):
						if rh < rt:
							rt = rh
							ct = ch
						rh -= 1
						visited.add((rt, ct))
				case 'D':
					for _ in range(step):
						if rh > rt:
							rt = rh
							ct = ch
						rh += 1
						visited.add((rt, ct))

		return len(visited)

		



print(solve())


def ten_knots():
	with open("input.txt") as f:
		knots = [[0,0] for _ in range(10)]
		visited = set()

		lines = f.read().strip().splitlines()
		
		for line in lines:
			direction, step = line.split(' ')
			step = int(step)
			
			for _ in range(step):
				knots[0] = move_head(knots[0], direction)

				for i in range(1, 10):
					knots[i] = move_tail(knots[i-1], knots[i])

				visited.add(tuple(knots[-1]))
			

		return len(visited)



sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)


def move_tail(h, t):
	[rh, ch] = h
	[rt, ct] = t

	dr, dc = rh-rt, ch-ct
	if dr == 0 or dc == 0:
		if abs(dr) >= 2:
			rt += sign(dr)
		if abs(dc) >= 2:
			ct += sign(dc)
	elif (abs(dr), abs(dc)) != (1, 1):
		rt += sign(dr)
		ct += sign(dc)

	return rt, ct

	
def move_head(h, direction):
	[rh, ch] = h
	match direction:
		case 'L':
			ch -= 1
		case 'R':
			ch += 1
		case 'U':
			rh -= 1
		case 'D':
			rh += 1
	return rh, ch



print(ten_knots())