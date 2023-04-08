from collections import deque

def solve(chars, start, end, check):
	R, C = len(chars), len(chars[0])
	start_r, start_c = 0, 0


	height = {chr(c): c-ord('a')+1 for c in range(ord('a'), ord('z')+1)}
	height['S'] = height['a']
	height['E'] = height['z']

	end_chars = set()
	for c, h in height.items():
		if h == height[end]:
			end_chars.add(c)
	

	def bfs(root):
		queue = deque([root])
		direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		step = 0
		visited = set()

		while queue:
			size = len(queue)
			for _ in range(size):
				r, c = queue.popleft()
				
				if (r, c) in visited:
					continue
				
				if chars[r][c] in end_chars:
					return step

				visited.add((r, c))
				cur_height = height[chars[r][c]]


				for [ri, ci] in direction:
					new_r, new_c = r+ri, c+ci
					
					if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
						continue

					if (new_r, new_c) in visited:
						continue
					
					new_height = height[chars[new_r][new_c]]
					if check(new_height - cur_height):
						queue.append([new_r, new_c])

			step += 1



	for r in range(R):
		for c in range(C):
			if chars[r][c] == start:
				start_r, start_c = r, c
				break

	return bfs([start_r, start_c])
			

with open("input.txt") as f:
	chars = [list(line) for line in f.read().split("\n")[:-1]]
	
	print(solve(chars, 'S', 'E', (lambda diff: diff <= 1)))
	print(solve(chars, 'E', 'a', (lambda diff: diff >= -1)))



