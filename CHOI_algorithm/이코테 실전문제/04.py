# 만들 수 없는 금액

# 2회차
# 답은 맞을 것 같지만 좀 더 간단하게 조건을 짤 수 있어야 한다
def tr1():
	n = int(input())
	coins = list(map(int, input().split()))
	max_num = 0

	coins.sort()
	for coin in coins:
		if coin <= max_num or coin == max_num + 1: 
			max_num += coin
		else:
			break
	print(max_num + 1)





tr1()





# 답
# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort()
# A = 1
# for B in coins:
# 	if A < B:
# 		break
# 	A += B
# print(A)
		




# 1회차
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




"""
testcase

5
3 2 1 1 9
asnwer : 8

9
1 1 1 1 1 1 1 1 1
answer : 10

4
2 3 4 5
answer : 1

4
1 3 2 7
answer : 14

"""