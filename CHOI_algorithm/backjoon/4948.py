# https://www.acmicpc.net/problem/4948

# tr 2
import sys

def is_prime(n):
	if n <= 1:
		return 0
	elif n == 2 or n == 3:
		return 1
	for i in range(2, int(n ** (0.5)) + 1):
		if n % i == 0:
			return 0
	return 1

prime = [0]
for i in range(1, 123456 * 2 + 1):
	if is_prime(i):
		prime.append(0)
	else:
		prime.append(i)

while True:
	n = int(sys.stdin.readline())
	ret = 0
	if n <= 0:
		break
	for i in range(n + 1, 2 * n + 1):
		if prime[i] == 0:
			ret += 1
	print(ret)




# # tr1 runtime error

# def is_prime(n):
# 	if n <= 1:
# 		return 0
# 	elif n == 2 or n == 3:
# 		return 1
# 	for i in range(2, int(n ** (1/2)) + 1):
# 		if n % i == 0:
# 			return 0
# 	return 1

# while True:
# 	n = int(input())
# 	ret = 0
# 	if n <= 0:
# 		break
# 	for i in range(n + 1, 2 * n + 1):
# 		if is_prime(i):
# 			ret += 1
# 	print(ret)





