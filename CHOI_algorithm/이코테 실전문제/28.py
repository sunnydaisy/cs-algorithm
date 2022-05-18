# 고정점 찾기

def binary_search(arr, start, end):
	if start > end:
		return -1
	mid = (start + end) // 2
	if arr[mid] == mid:
		return mid
	elif arr[mid] < mid: # 오른쪽으로 가야하는 경우
		return binary_search(arr, mid + 1, end)
	else:
		return binary_search(arr , start, mid - 1)


def solution():
	n = int(input())
	arr = list(map(int, input().split()))
	print(binary_search(arr, 0, n - 1))


"""
5
-15 -6 1 3 7
결과 : 3

7
-15 -4 2 8 9 13 15
result : 2


7
-15 -4 3 8 9 13 15
result : -1





"""




# --------------- 시도 1 : 시간초과
# def solution():
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	for i in arr:
# 		if i < 0:
# 			continue
# 		if i < len(arr) and arr[i] == i:
# 			return i
# 	return -1

solution()