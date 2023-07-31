stacks = [
	['C','Q','B'],
	['Z', 'W',' Q', 'R'],
	['V', 'L', 'R', 'M', 'B'],
	['W','T','V','H','Z','C'],
	['G','V','N','B','H','Z','D'],
	['Q','V','F','J','C','P','N','H'],
	['S','Z','W','R','T','G','D'],
	['P','Z','W','B','N','M','G','C'],
	['P','F','Q','W','M','B','J','N']
]

for i in range(len(stacks)):
	stacks[i].reverse()

def mover():
	with open("input.txt") as f:
		data = f.read()
		init, instructions = data.split('\n\n')
		for line in instructions[:-1].split('\n'):
			temp = line.split(' ')
			num, s1, s2 = [int(temp[i]) for i in range(1, len(temp), 2)]
			for _ in range(num):
				stacks[s2-1].append(stacks[s1-1].pop())
	
	res = ''
	for s in stacks:
		res += s[-1]
	print(res)
		

def mover_same_order():
	with open("input.txt") as f:
		data = f.read()
		init, instructions = data.split('\n\n')
		for line in instructions[:-1].split('\n'):
			temp = line.split(' ')
			num, s1, s2 = [int(temp[i]) for i in range(1, len(temp), 2)]
			print(num, s1, s2)
			stacks[s2-1].extend(stacks[s1-1][-1-num+1:])
			stacks[s1-1] = stacks[s1-1][:-1-num+1]
			print(stacks)
			
	
	res = ''
	for s in stacks:
		res += s[-1]
	print(res)


mover_same_order()