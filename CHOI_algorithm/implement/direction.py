n = int(input())
plan = list(input().split())
now = [0, 0]

for dir in plan:
	if dir == 'U' and now[1] != 0:
		now[1] -= 1
	elif dir == 'D' and now[1] != n - 1:
		now[1] += 1
	elif dir == 'L' and now[0] != 0:
		now[0] -= 1
	elif dir == 'R' and now[0] != n - 1:
		now[0] += 1
print(now[1] + 1, now[0] + 1)