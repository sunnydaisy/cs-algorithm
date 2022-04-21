# 감시 피하기
# https://www.acmicpc.net/problem/18428

import sys
from itertools import permutations, combinations
from collections import deque

def check(graph, n):
	q = deque()
	for i in range(n):
		for j in range(n):
			if graph[i][j] == 'T':
				tx = i
				ty = j
				while tx >= 0:
					if graph[tx][ty] == 'O':
						break
					if graph[tx][ty] == 'S':
						return False
					tx -= 1
				tx = i
				while tx < n:
					if graph[tx][ty] == 'O':
						break
					if graph[tx][ty] == 'S':
						return False
					tx += 1
				tx = i
				while ty >= 0:
					if graph[tx][ty] == 'O':
						break
					if graph[tx][ty] == 'S':
						return False
					ty -= 1
				ty = j
				while ty < n:
					if graph[tx][ty] == 'O':
						break
					if graph[tx][ty] == 'S':
						return False
					ty += 1
	return True
					

def dfs(graph, n, count):
	if count == 3:
		if check(graph, n):
			return True
		return False
	else:
		for i in range(n):
			for j in range(n):
				if graph[i][j] == 'X':
					graph[i][j] = 'O'
					if dfs(graph, n, count + 1):
						return True
					graph[i][j] = 'X'

def solution():
	n = int(input())
	graph = []
	for _ in range(n):
		graph.append(list(sys.stdin.readline().split()))
	if dfs(graph,  n, 0):
		print("YES")
	else:
		print("NO")

solution()