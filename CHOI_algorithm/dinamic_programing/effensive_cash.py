import sys

# 해설

def solution():

	n, m = map(int, input().split())
	coins = []
	for _ in range(n):
		coins.append(int(sys.stdin.readline().rstrip()))
	
	d = [10001] * (m + 1)
	for i in coins:
		d[0] = 0
		for j in range(i, m + 1):
			if d[j - i] != 10001:
				d[j] = min(d[j], d[j - i] + 1)
	if d[m] == 10001:
		print(-1)
	else:
		print(d[m])



# 시도 1
# def solution():

# 	n, m = map(int, input().split())
# 	coins = []
# 	for _ in range(n):
# 		coins.append(int(sys.stdin.readline().rstrip()))

# 	coins.sort(reverse=True)
# 	count = 0

# 	for i in coins:
# 		count += m // i
# 		m = m % i
# 		if m == 0:
# 			return count
# 	return -1

print(solution())