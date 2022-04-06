# 모험가 길드

# 2회

def tr_1():
	n = int(input())
	group = list(map(int, input().split()))

	group.sort()

	result = 0
	count = 0
	for i in group:
		count += 1
		# if count == i:  이렇게 했었는데 답을 보니까 아래 방식이 더 맞는듯 하다.
		if count >= i:  
			result += 1
			count = 0
	print(result)

tr_1()






# 답
# n = int(input())
# pobia = list(map(int, input().split()))

# pobia.sort()
# result = 0
# count = 0

# for i in pobia:
# 	count += 1
# 	if count >= i:
# 		result += 1
# 		count = 0
# print(result)




# 1차 풀이 (틀림)
# n = int(input())
# pobia = list(map(int, input().split()))

# result = 0
# last = 0
# set_pobia = set(pobia)

# for i in set_pobia:
# 	ct = pobia.count(i)
# 	result += (ct + last) // i
# 	last = (ct + last) % i
# print(result)



"""
테스트 케이스

5
2 3 1 2 2
answer : 2

7
1 1 1 1 1 1 1
answer : 7

6
6 6 6 6 6 8
answer = 0

"""