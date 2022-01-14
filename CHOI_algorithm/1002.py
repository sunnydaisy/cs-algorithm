def distance(x_1, y_1, x_2, y_2):
	x = x_1 - x_2
	y = y_1 - y_2
	return (x**2 + y**2)**0.5

def solution(a, b):
	""" a > b"""
	detween = distance(*a[:2], *b[:2])
	if detween == 0 and a[2] == b[2]:
		return -1
	elif detween > a[2] + b[2]:
		"""원이 서로 안 닿을 떄"""
		return 0
	elif detween == a[2] + b[2]:
		"""원이 서로 바깥에서 닿을 때"""
		return 1
	elif detween < a[2] + b[2]:
		if detween + b[2] > a[2]:
			return 2
		elif detween + b[2] == a[2]:
			"""원이 안쪽에서 서로 닿을 떄"""
			return 1
		else:
			return 0

for _ in range(int(input())):
	x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
	if r_1 >= r_2:
		print(solution([x_1, y_1, r_1], [x_2, y_2, r_2]))
	else:
		print(solution([x_2, y_2, r_2], [x_1, y_1, r_1]))
