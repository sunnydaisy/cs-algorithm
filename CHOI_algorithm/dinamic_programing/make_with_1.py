# 내 풀이

# def solution():
# 	n = int(input())

# 	dp = [0] * (n + 1)
# 	dp[1] = 1
# 	dp[2] = 1
# 	dp[3] = 1
# 	dp[4] = 2
# 	dp[5] = 1

# 	for i in range(6, n + 1):
# 		ck = []
# 		if i % 5 == 0:
# 			ck.append(dp[i // 5])
# 		if i % 3 == 0:
# 			ck.append(dp[i // 3])
# 		if i % 2 == 0:
# 			ck.append(dp[i // 2])
# 		ck.append(dp[i - 1])
# 		dp[i] = min(ck) + 1

# 	print(dp[n]) 

# solution()



# 답지

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
	d[i] = d[i - 1] + 1
	if i % 2 == 0:
		d[i] = min(d[i], d[i // 2] + 1)
	if i % 3 == 0:
		d[i] = min(d[i], d[i // 3] + 1)
	if i % 5 == 0:
		d[i] = min(d[i], d[i // 5] + 1)

print(d[x])