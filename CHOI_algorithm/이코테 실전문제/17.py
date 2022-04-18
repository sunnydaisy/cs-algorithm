# 경쟁적 감염
# https://www.acmicpc.net/problem/18405



# ---------------------------- 1회차 : 정답 664ms
# import sys
# import heapq
# import copy

# def bfs(graph, tmp_list, s):
# 	time = 0	# 현재 시간
# 	now = 0		# 지금까지 진행한 개수
# 	n = len(graph)	# 맵 크기 (n)
# 	queue = []
# 	tmp = []
# 	if time == s: # 0 초인 경우
# 		return
# 	for x, y  in tmp_list:
# 		heapq.heappush(queue, (graph[x][y], x + 1, y))
# 		heapq.heappush(queue, (graph[x][y], x - 1, y))
# 		heapq.heappush(queue, (graph[x][y], x, y + 1))
# 		heapq.heappush(queue, (graph[x][y], x, y - 1))
# 	while queue:
# 		now += 1
# 		virus , vx, vy = heapq.heappop(queue)
# 		if vx >= 0 and vy >= 0 and vx < n and vy < n:
# 			if graph[vx][vy] == 0: # 비어있을 떄
# 				graph[vx][vy] = virus
# 				heapq.heappush(tmp, (virus, vx + 1, vy))
# 				heapq.heappush(tmp, (virus, vx - 1, vy))
# 				heapq.heappush(tmp, (virus, vx, vy + 1))
# 				heapq.heappush(tmp, (virus, vx, vy - 1))
# 		if len(queue) <= 0:
# 			queue = copy.deepcopy(tmp)
# 			tmp = []
# 			time += 1
# 			if time == s: # 시간이 되었을 떄
# 				return




# def solution():
# 	n, k = map(int, input().split())
# 	graph = []
# 	for _ in range(n):
# 		graph.append(list(map(int, sys.stdin.readline().split())))
# 	s, rx, ry = map(int, input().split())
	
# 	tmp_list = []
# 	for i in range(n):
# 		for j in range(n):
# 			if graph[i][j] != 0: # 바이러스인 경우
# 				tmp_list.append((i, j))
# 	bfs(graph, tmp_list, s)
# 	return graph[rx - 1][ry - 1]

# print(solution())