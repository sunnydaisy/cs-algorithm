# 정렬된 배열에서 특정 수의 개수 구하기

def left_search(arr, target, start, end):
	mid = (end + start) // 2
	if start > end:
		return None
	
	if (mid == 0 or arr[mid - 1] < target)  and arr[mid] == target:
		return mid
	elif arr[mid] >= target:
		return left_search(arr, target, start, mid - 1)
	else:
		return left_search(arr, target, mid + 1, end)
	

def right_search(arr, target, start, end):
	mid = (end + start) // 2
	if start > end:
		return None
	
	if (mid == n - 1 or arr[mid + 1] > target)  and arr[mid] == target:
		return mid
	elif arr[mid] > target:
		return right_search(arr, target, start, mid - 1)
	else:
		return right_search(arr, target, mid + 1, end)
	



n, x = map(int, input().split())


def solution():
	arr = list(map(int, input().split()))
	a = right_search(arr, x, 0, n - 1)
	if a == None:
		print(-1)
		return
	result =  left_search(arr, x, 0, n - 1) - a + 1
	print(result)
	

solution()


# 풀이 1 : bisect 활용
# from bisect import bisect_left, bisect_right

# def solution():
# 	n, x = map(int, input().split())
# 	arr = list(map(int, input().split()))
# 	result = bisect_right(arr, x) - bisect_left(arr, x)
# 	if result == 0:
# 		print(-1)
# 	else:
# 		print(result)
# solution()