# 인구 이동
# https://www.acmicpc.net/problem/16234

import sys

n, l, r = map(int, input().split())

def bfs(graph, x, y, visited, before):
	if x < 0 or y < 0 or x >= n or y >= n:
		return 0, 0
	if visited[x][y] == True:
		return 0, 0
	if l <= (graph[x][y] - before) and (graph[x][y] - before) <= r:
		tmp = graph[x][y]
		visited[x][y] = True
		ct = 1
		result = bfs(graph, x + 1, y, visited, graph[x][y])
		tmp += int(result[0])
		ct += result[1]
		result = bfs(graph, x - 1, y, visited, graph[x][y])
		tmp += result[0]
		ct += result[1]
		result = bfs(graph, x, y + 1, visited, graph[x][y])
		tmp += result[0]
		ct += result[1]
		result = bfs(graph, x, y - 1, visited, graph[x][y])
		tmp += result[0]
		ct += result[1]
		return (tmp, ct)
	return 0, 0

def op(graph):
	visited = [[False] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			tmp, ct = bfs(graph, i, j, visited, graph[i][j])
			if ct > 1: # 인접한게 있었을 때
				for rx in range(n):
					for ry in range(n):
						if visited[rx][ry] == True:
							graph[rx][ry] = int(tmp / ct)
							visited[rx][ry] = False
				return ct

def solution():
	graph = []
	for _ in range(n):
		graph.append(list(map(int, sys.stdin.readline().split())))
	visited = [[False] * n for _ in range(n)]
	count = 1
	final = n * n
	while count <= 2000:
		if op(graph) == final:
			return count
		count += 1
	return 0



print(solution())