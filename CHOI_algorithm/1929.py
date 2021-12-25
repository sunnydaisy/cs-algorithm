def prime_ck(num):
	if num < 2:
		return
	max = int(num ** (1 / 2))
	for j in range(2, max + 1):
		if num % j == 0:
			return
	print(num)

m, n = map(int, input().split())

for i in range(m, n + 1):
	prime_ck(i)
