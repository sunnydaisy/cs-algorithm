# 동전 0

n, k = map(int, input().split())
coin_type = []
result = 0

for _ in range(n):
	coin_type.append(int(input()))

coin_type.sort(reverse=True)
for i in coin_type:
	if i > k:
		continue
	result +=  k // i
	k %= i

print(result)
