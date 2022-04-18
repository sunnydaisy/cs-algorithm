# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

# ------------------------------- 해설 1604ms
# from collections import deque
# import sys

# def solution():
# 	n, m, k, x = map(int, input().split())
# 	graph = [[] for _ in range(n + 1)]

# 	for _ in range(m):
# 		a, b = map(int, sys.stdin.readline().split())
# 		graph[a].append(b)
# 	distance = [-1] * (n + 1)
# 	distance[x] = 0

# 	q = deque([x])
# 	while q:
# 		now = q.popleft()
# 		for next_node in graph[now]:
# 			if distance[next_node] == -1:
# 				distance[next_node] = distance[now] + 1
# 				q.append(next_node)

# 	ckeck = False
# 	for i in range(1, n + 1):
# 		if distance[i] == k:
# 			print(i)
# 			ckeck = True
# 	if ckeck == False:
# 		print(-1)
# solution()






# ----------------------------- 1회차 정답 1320ms
# import sys
# from collections import deque

# def bfs(graph, start, visited, target):
# 	queue = deque()
# 	queue.append((start, 0))
# 	visited[start] = True
# 	result = []
# 	while queue:
# 		node = queue.popleft()
# 		v, cost = node[0], node[1]
# 		if cost == target:
# 			result.append(v)
# 			continue
# 		for j in graph[v]:
# 			if not visited[j]:
# 				visited[j] = True
# 				queue.append((j, cost + 1))
# 	result.sort()
# 	return result


# def soultion():
# 	n, m, k, x = map(int, input().split())
# 	graph = [[] for _ in range(n + 1)]
# 	visited = [False] * (n + 1)

# 	for _ in range(m):
# 		start, end = map(int, sys.stdin.readline().split())
# 		graph[start].append(end)

# 	result = bfs(graph, x, visited, k)
# 	if len(result) <= 0:
# 		print(-1)
# 	else:
# 		for i in result:
# 			print(i)
# soultion()