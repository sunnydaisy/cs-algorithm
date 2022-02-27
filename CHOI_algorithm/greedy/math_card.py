# 숫자 카드

N, M = map(int, input().split())
result = 0

for _ in range(N):
	date = list(map(int, input().split()))
	min_value = min(date)
	result = max(result, min_value)


print(min_value)