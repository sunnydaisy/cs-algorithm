# 안테나
# https://www.acmicpc.net/problem/18310


def solution():
	n = int(input())
	house = map(int, input().split())
	num_list = [0] * 100001
	for i in house:
		num_list[i] += 1
	result = int(1e9)
	for i in range(1, 100001):
		if num_list[i] > 0:
			result = 0
			for j in range(1, 100001):
				

solution()