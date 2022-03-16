import sys

# 이진 탐색 풀이

# def binary_search(array, target, start, end):
# 	while start <= end:
# 		mid = (end + start) // 2
# 		if array[mid] == target:
# 			return True
# 		elif array[mid] > target:
# 			end = mid - 1
# 		else:
# 			start = mid + 1
# 	return False

# n = int(sys.stdin.readline().rstrip())
# n_list = list(map(int, sys.stdin.readline().rstrip().split()))

# m = int(sys.stdin.readline().rstrip())
# m_list = list(map(int, sys.stdin.readline().rstrip().split()))

# n_list.sort()
# m_list

# for i in m_list:
# 	if binary_search(n_list, i, 0, len(n_list) - 1):
# 		print('yes', end=' ')
# 	else:
# 		print('no', end=' ')


# 계수 정렬 풀이

# n = int(sys.stdin.readline().rstrip())
# n_list = list(map(int, sys.stdin.readline().rstrip().split()))

# m = int(sys.stdin.readline().rstrip())
# m_list = list(map(int, sys.stdin.readline().rstrip().split()))

# array = [0] * (max(n_list) + 1)

# for i in n_list:
# 	array[i] += 1

# for i in m_list:
# 	if array[i] > 0:
# 		print('yes', end=' ')
# 	else:
# 		print('no', end=' ')



# set 를 사용하는 방법

n = int(input())
n_list = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in m_list:
	if i in n_list:
		print('yes', end=' ')
	else:
		print('no', end=' ')
