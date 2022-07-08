# https://www.acmicpc.net/problem/13460
# 구슬 탈출2

import sys

input = sys.stdin.readline
n, m =map(int, input().split())
min_time = int(1e9)

def solution():
	graph = []

	for _ in range(n):
		line = input().split()
		graph.append(line)
	
	visited = []

def dfs(graph, visited, pos, time):
	visited.append(pos)
	r_pos = pos[0]
	b_pos = pos[1]
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]


	# add
	for i in range(4):
		# t_pos = moving(i)
		t_pos = []
		if (!t_pos):
			continue
		if t_pos in visited:
			continue
		if t_pos[0][0] < 0 ..:
			continue
		dfs(graph, visited, t_pos, time + 1)

	visited.pop()



solution()