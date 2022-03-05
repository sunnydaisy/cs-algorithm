# 모험가 길드

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


n = int(input())
pobia = list(map(int, input().split()))

pobia.sort()
result = 0
count = 0

for i in pobia:
	count += 1
	if count >= i:
		result += 1
		count = 0
print(result)