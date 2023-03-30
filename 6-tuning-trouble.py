def first_n(n):
	with open("input.txt") as f:
		s = f.read()
		
		d = {}
		l, r = 0, 0
		while r < len(s):
			if s[r] not in d:
				d[s[r]] = r
			elif d[s[r]] >= l:
				l = d[s[r]]+1
				d[s[r]] = r
			else:
				d[s[r]] = r
			if r - l == n-1:
				return r+1
			r += 1

print(first_n(4))
print(first_n(14))