# 만들 수 없는 금액


# 1차 시도(Fail)

# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort()
# result = 0
# count = 1
# type = []

# for idx, coin in enumerate(coins):
# 	type.append(coin)
# 	if idx < len(coins) - 1:
# 		for i in coins[idx + 1:]:


n = int(input())
coins = list(map(int, input().split()))
coins.sort()
A = 1
for B in coins:
	if A < B:
		break
	A += B
print(A)
		