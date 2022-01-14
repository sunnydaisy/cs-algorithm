from sys import stdin


def solution(arr, n):
	m = n // 2
	for i in range(m + 1):
		if arr[m - i] is True and arr[m + i] is True:
			return [m - i, m + i]

arr = [False, False] + [True] * 9999

for i in range(2, 101):
	if arr[i]:
		for j in range(i*2, len(arr), i):
			arr[j] = False

for _ in range(int(stdin.readline())):
	t = int(stdin.readline())
	print(*solution(arr, t))
