'''
pair index starts from 1
'''

def solve():
	res = 0
	with open("input.txt") as f:
		pairs = f.read().split("\n\n")
		for i in range(len(pairs)):
			pair = pairs[i]
			l1, l2 = [(lambda s: eval(s))(lst) for lst in pair.splitlines()]
			if is_right_order(l1, l2) < 0:
				res += i+1
		return res
			


def is_right_order(l1, l2):
	if type(l1) is int and type(l2) is int:
		return l1 - l2
	elif type(l1) is list and type(l2) is list:
		i = 0
		border = min(len(l1), len(l2))
		while i < border:
			res = is_right_order(l1[i], l2[i])
			if res != 0:
				return res

			i += 1
		return len(l1) - len(l2)
	elif type(l1) is int and type(l2) is list:
		return is_right_order([l1], l2)
	elif type(l1) is list and type(l2) is int:
		return is_right_order(l1, [l2])



def decoder_key():
	with open("input.txt") as f:
		pairs = f.read().split("\n\n")
		all_pairs = []
		for i in range(len(pairs)):
			pair = pairs[i]
			l1, l2 = [(lambda s: eval(s))(lst) for lst in pair.splitlines()]
			all_pairs.extend([l1, l2])

		all_pairs.extend([[[2]], [[6]]])

		for i in range(len(all_pairs)):
			for j in range(len(all_pairs)-1):
				if is_right_order(all_pairs[j], all_pairs[j+1]) > 0:
					all_pairs[j], all_pairs[j+1] = all_pairs[j+1], all_pairs[j]


		two, six = [i+1 for i in range(len(all_pairs)) if all_pairs[i] == [[2]] or all_pairs[i] == [[6]]]
		return two * six



print(solve())
print(decoder_key())
