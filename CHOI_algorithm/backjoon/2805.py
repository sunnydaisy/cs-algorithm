# 나무 자르기 문제
import sys

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