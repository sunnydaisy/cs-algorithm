# 안테나
# https://www.acmicpc.net/problem/18310


def solution():
	n = int(input())
	house = list(map(int, input().split()))
	house.sort()
	print(house[(n - 1) // 2])
solution()

# --------------------------- 2회차 : 실패
# def search(array, target):
# 	i = 1
# 	while i < len(array):
# 		if 0 <= target - i < len(array) and array[target - i] > 0:
# 			return target - i
# 		elif  0 <= target + i < len(array) and array[target + i] > 0:
# 			return target + i
# 		i += 1

# def solution():
# 	n = int(input())
# 	house = list(map(int, input().split()))
# 	mean = sum(house) // n
# 	if mean in house:
# 		return mean
# 	# house.sort()
# 	num_list = [0] * 100001
# 	for i in house:
# 		num_list[i] += 1
	
# 	return search(num_list, mean)
"""
1 2 2 5 9
중간값 : 3.8
안테나 2 -> 11
안테나 5 -> 12

1 2 2 5 10
중간값 : 4
안테나 2 -> 12
안테나 5 -> 15
"""


# ------------------ 1회차 : 실패 (시간초과)
# def solution():
# 	n = int(input())
# 	house = list(map(int, input().split()))
# 	num_list = [0] * 100001
# 	for i in house:
# 		num_list[i] += 1
# 	min_num = int(1e9)
# 	result = -1
# 	for i in range(1, 100001):
# 		if num_list[i] > 0:
# 			tmp = 0
# 			for j in list(set(house)):
# 				tmp += abs(i - j) * num_list[j]
# 			if min_num > tmp:
# 				min_num = tmp
# 				result = i
# 	print(result)
# 	return result
print(solution())