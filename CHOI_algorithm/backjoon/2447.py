def solution(n):
	if n == 1:
		return ['*']
	star = solution(n // 3)
	l = []
	for s in star:
		l.append(s*3)
	for s in star:
		l.append(s + ' '*(n//3) + s)
	for s in star:
		l.append(s*3)
	return l

n = int(input())
map = solution(n)
for i in map:
	print(i)
