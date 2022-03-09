# 덩치 문제
import sys

n = int(sys.stdin.readline())
l = []

for i in range(n):
	tmp = list(map(int, sys.stdin.readline().split())) 
	tmp.insert(0, 1)
	l.append(tmp)


for i in l:
	for j in l:
		if i[1] > j[1] and i[2] > j[2]:
			j[0] += 1
		# elif ((i[1] > j[1] and i[2] == j[2]) or (i[1] == j[1] and i[2] > j[2])):
		# 	j[0] += 1


for idx, i in enumerate(l):
	if idx == 0:
		print(i[0], end='')
	else:
		print('', i[0], end='')
print()

