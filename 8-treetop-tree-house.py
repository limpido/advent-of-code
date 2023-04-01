def count_visible_trees():
	res = 0
	with open("input.txt") as f:
		lines = f.readlines()
		trees = [line[:-1] for line in lines]
		ROW, COL = len(trees), len(trees[0])
		res += ROW*2 + COL*2 - 4
		visible = set()

		# left
		for r in range(1, ROW-1):
			largest = trees[r][0]
			for c in range(1, COL-1):
				if trees[r][c] > largest:
					largest = trees[r][c]
					visible.add((r, c))

		# right
		for r in range(ROW-2, 0, -1):
			largest = trees[r][COL-1]
			for c in range(COL-2, 0, -1):
				if (r, c) in visible:
					largest = max(largest, trees[r][c])
					continue
				if trees[r][c] > largest:
					largest = trees[r][c]
					visible.add((r, c))


		# top
		for c in range(1, COL-1):
			largest = trees[0][c]
			for r in range(1, ROW-1):
				if (r, c) in visible:
					largest = max(largest, trees[r][c])
					continue
				if trees[r][c] > largest:
					largest = trees[r][c]
					visible.add((r, c))


		# bottom
		for c in range(1, COL-1):
			largest = trees[ROW-1][c]
			for r in range(ROW-2, 0, -1):
				if (r, c) in visible:
					largest = max(largest, trees[r][c])
					continue
				if trees[r][c] > largest:
					largest = trees[r][c]
					visible.add((r, c))

	res += len(visible)
	print(res)



def highest_scenic_score():
	with open("input.txt") as f:
		lines = f.readlines()
		trees = [line[:-1] for line in lines]
		ROW, COL = len(trees), len(trees[0])
		
		res = 0
		for r in range(ROW):
			for c in range(COL):
				# left
				left = 0
				for i in range(c-1, -1, -1):
					left += 1
					if trees[r][i] >= trees[r][c]:
						break

				# right
				right = 0
				for i in range(c+1, COL):
					right += 1
					if trees[r][i] >= trees[r][c]:
						break

				# top
				top = 0
				for i in range(r-1, -1, -1):
					top += 1
					if trees[i][c] >= trees[r][c]:
						break

				# bottom
				bottom = 0
				for i in range(r+1, ROW):
					bottom += 1
					if trees[i][c] >= trees[r][c]:
						break

				res = max(res, left*right*top*bottom)
		print(res)



highest_scenic_score()