import time

# 일반적 재귀 방법 (x = 40 일 때 13.18ms)
# def fibo(x):
# 	if x == 1 or x == 2:
# 		return 1
# 	return fibo(x - 1) + fibo(x - 2)




# Memoization 방법 (x = 40 일 때 3.19ms)
# d = [0] * 100

# def fibo(x):
# 	if x == 1 or x == 2:
# 		return 1

# 	if d[x] != 0:
# 		return d[x]
# 	d[x] = fibo(x - 1) + fibo(x - 2)
# 	return d[x]

# start = time.time()
# print(fibo(40))
# print(time.time() - start)




# 보텀업 방식
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
	d[i] = d[i - 1] + d[i - 2]

print(d[n])



