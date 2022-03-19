from calendar import c


n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

def solution(x):
	for i in range(2, n):
		d[i] = (d[i - 2] * 2 + d[i - 1]) % 796796
