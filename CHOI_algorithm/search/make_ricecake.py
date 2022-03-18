import sys

# 시도 (실패)
# def sum_left(array, length):
# 	result = 0
# 	for i in array:
# 		left = i - length
# 		if left <= 0:
# 			continue
# 		result += left
# 	return result

# def binary_search(array, target, min, max):
# 	while min <= max:
# 		mid = (min + max) // 2
# 		tmp = sum_left(array, mid)
# 		if tmp == target:
# 			return mid
# 		elif tmp > target:
# 			max = mid - 1
# 		else:
# 			min = mid + 1
# 	return -1



def solution():
	n , m = list(map(int, input().split()))
	array = list(map(int, sys.stdin.readline().rstrip().split()))


	start = 0
	end = max(array)

	result = 0
	while start <= end:
		mid = (start + end) // 2
		total = 0
		for i in array:
			if i > mid:
				total += i - mid
		if total < m: # 떡이 부족한 경우
			end = mid - 1
		else: 
			result = mid
			start = mid + 1

	print(result)
solution()