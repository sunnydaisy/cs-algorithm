n = int(input())


for i in range(n):
	x, y = map(int, input().split())
	len = y - x
	answer = 0
	for j in range(1, len + 1):
		ck = j * j + j
		if ck >= len :
			if ((j * j) >= len):
				answer = 2 * j - 1
			else:
				answer = 2 * j
			break
	print(answer)
