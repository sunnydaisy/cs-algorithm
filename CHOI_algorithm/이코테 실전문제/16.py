# 연구소
# https://www.acmicpc.net/problem/14502

# -------------------------------- 해설 : 시간초과??
# import sys

# n, m = map(int, input().split())

# def virus(x, y, temp):
# 	dx = [-1, 0, 1, 0]
# 	dy = [0, 1, 0, -1]

# 	for i in range(4):
# 		nx = x + dx[i]
# 		ny = y + dy[i]
# 		if nx >= 0 and ny >= 0 and nx < n and ny < m:
# 			if temp[nx][ny] == 0:
# 				temp[nx][ny] = 2
# 				virus(nx, ny, temp)

# def get_score(temp):
# 	score = 0
# 	for i in range(n):
# 		for j in range(m):
# 			if temp[i][j] == 0:
# 				score += 1
# 	return score
# result = 0
# def dfs(count, temp, data):
# 	global result
# 	if count == 3:
# 		for i in range(n):
# 			for j in range(m):
# 				temp[i][j] = data[i][j]
# 		for i in range(n):
# 			for j in range(m):
# 				if temp[i][j] == 2:
# 					virus(i, j, temp)
# 		result = max(result, get_score(temp))
# 		return
# 	for i in range(n):
# 		for j in range(m):
# 			if data[i][j] == 0:
# 				data[i][j] = 1
# 				count += 1
# 				dfs(count, temp, data)
# 				data[i][j] = 0
# 				count -= 1

# def solution():
# 	global result
# 	data = [] # 초기 맵
# 	temp = [[0] * m for _ in range(n)]

# 	for _ in range(n):
# 		data.append(list(map(int, sys.stdin.readline().split())))

# 	dfs(0, temp, data)
# 	return result






# ------------------------------------------------ 시도 2 : 정답 6480ms
# from itertools import combinations, permutations
# from collections import deque
# import copy

# n, m = map(int, input().split())

# def bfs(graph, x, y):
# 	queue = deque()
# 	# 처음에는 2가 오는 경우니까
# 	queue.append((x + 1, y))
# 	queue.append((x - 1, y))
# 	queue.append((x, y + 1))
# 	queue.append((x, y - 1))
# 	while queue:
# 		x, y = queue.popleft()
# 		if x < 0 or y < 0 or x >= n or y >= m:
# 			continue
# 		if graph[x][y] != 0:
# 			continue
# 		graph[x][y] = 2
# 		queue.append((x + 1, y))
# 		queue.append((x - 1, y))
# 		queue.append((x, y + 1))
# 		queue.append((x, y - 1))
		
	
# def solution():
# 	graph = []
# 	for _ in range(n):
# 		line = list(map(int, input().split()))
# 		graph.append(line)
# 	permutations_tmp = []
# 	result = 0
# 	# 경우의 수 넣기
# 	for i in range(n):
# 		for j in range(m):
# 			permutations_tmp.append((i, j))
# 	for pers in list(combinations(permutations_tmp, 3)):
# 		tmp_graph = copy.deepcopy(graph)
# 		flag = 0 # 기본값 0
# 		for x, y in pers:
# 			if tmp_graph[x][y] != 0:
# 				flag = 1
# 				break
# 			tmp_graph[x][y] = 1
# 		if flag == 1: # 3번 벽을 안넣은 경우 다른 조합 실행
# 			continue
# 		# if (0,1) in pers and (1, 0) in pers and (3, 6) in pers:
# 		# 	print("hi")
# 		for x in range(n):
# 			for y in range(m):
# 				if tmp_graph[x][y] == 2:
# 					bfs(tmp_graph, x, y)
# 		tmp_count = 0
# 		for x in range(n):
# 			for y in range(m):
# 				if tmp_graph[x][y] == 0:
# 					tmp_count += 1
# 		result = max(result, tmp_count)
# 	return result











# --------------------------------- 시도 1 : 실패 (DFS 로 하려고 했는데 최대 재귀를 넘어서 실패했다)
# from itertools import permutations
# import copy

# def dfs(graph, x, y):
# 	if x < 0 or y < 0 or x >= n or y >= m:
# 		return 0
# 	if graph[x][y] != 1: # 벽만 아니면 됨
# 		graph[x][y] = 2
# 		count = 1
# 		count += dfs(graph, x - 1, y)
# 		count += dfs(graph, x + 1, y)
# 		count += dfs(graph , x, y - 1)
# 		count += dfs(graph, x, y + 1)
# 		return count
# 	return 0
	
	
# n, m = map(int, input().split())
# def solution():
# 	graph = []
# 	result = 0
# 	for _ in range(n):
# 		line = list(map(int, input().split()))
# 		graph.append(line)
# 	combination = []
# 	for i in range(n):
# 		for j in range(m):
# 			combination.append((i, j))
	
# 	for lines in list(permutations(combination, 3)):
# 		count = 0
# 		tmp_result = 0
# 		tmp = copy.deepcopy(graph)
# 		for x, y in lines: # 벽 3개 새우기
# 			if tmp[x][y] == 0:
# 				tmp[x][y] = 1
# 				count += 1
# 		if count < 3: # 3개 안새웠으면 다시 지우고 다른 경우의 수 보기
# 			for x, y in lines:
# 				if tmp[x][y] == 1:
# 					tmp[x][y] = 0
# 			continue
# 		for i in range(n):
# 			for j in range(m):
# 				if tmp[i][j] == 2:
# 					tmp_result += dfs(graph, i, j)
# 		result = max(result, tmp_result)
# 	return result

	
	

print(solution())
