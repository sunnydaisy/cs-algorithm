import sys

def binary_search(array, target, start, end):
	
	mid = (array[start] + array[end]) // 2
	tmp = sum(array[start:]) - mid * len(array[start:])
	if tmp == 0:
		return None
	if tmp == target:
		return mid
	elif tmp > target:
		if tmp > binary_search(array, target, (start + end) // 2, end):
			return tmp
		else:
			pass
	else:
		binary_search(array, target, start, (start + end) // 2)

n , m = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()
a = binary_search(array, m, 0, n - 1)
print(a)
