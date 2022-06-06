# 아기 상어
# https://www.acmicpc.net/problem/16236

# ------------------------------- 2회차 성공
# 모든 조건에 맞게 구현하면 된다. n 의 크기가 크지 않으므로 
import sys
import heapq

input = sys.stdin.readline

n = int(input())
INF = int(1e9)

def bfs(graph, shark):
	q = []
	
	s_x, s_y, s_size = shark[0], shark[1], shark[2]
	dx = [0, 1, 0, -1]
	dy = [-1, 0, 1, 0]
	visited = [[0] * n for _ in range(n)]
	
	heapq.heappush(q, (0, s_x, s_y))
	min_time, min_pos = INF, []
	while q:
		time, x, y = heapq.heappop(q)
		# 방문표시
		if visited[x][y] != 0:
			continue
		else:
			visited[x][y] = 1
		
		# 최소시간보다 큰 경우
		if time > min_time or time > n * n:
			break
		
		# 먹을 수 있는 물고기를 만난 경우
		if graph[x][y] != 0 and graph[x][y] < s_size and [x, y] not in min_pos:
			min_time = time
			if len(min_pos) > 0:
				min_pos.append([x, y])
			else:
				min_pos = [[x, y]]
			continue
					
		for i in range(4):
			nx = dx[i] + x
			ny = dy[i] + y
			if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] > s_size:
				continue
			heapq.heappush(q, (time + 1, nx, ny))
	# 하나도 안먹은 경우
	if len(min_pos) == 0:
		return [INF, INF, -1]
	# 후보가 여러개인 경우
	elif len(min_pos) > 1:
		min_pos.sort(key=lambda x : (x[0], x[1]))

	x, y = min_pos[0]
	graph[x][y] = 0
	return [x, y, min_time]

	


def solution():
	
	graph = []
	for _ in range(n):
		graph.append(list(map(int, input().split())))
	
	# 상어 위치 찾기
	for i in range(n):
		for j in range(n):
			if graph[i][j] == 9:
				shark = [i, j, 2]
				graph[i][j] = 0
	time = 0
	eat_count = 0
	
	while True:
		f_x, f_y, cost = bfs(graph, shark)
		if f_x == INF:
			break
		graph[f_x][f_y] = 0
		eat_count += 1
		# 상어가 커져야 할 때
		if eat_count == shark[2]:
			shark = [f_x, f_y, shark[2] + 1]
			eat_count = 0
		# 일반적인 경우
		else:
			shark = [f_x, f_y, shark[2]]
			
		time += cost
	print(time)
solution()

# ---------------------------------------------------- 1회차 실패
# import sys
# from collections import deque
# input = sys.stdin.readline

# def distance(sark, point):
# 	return abs(sark[0] - point[0]) + abs(sark[1] - point[1])

# def solution():
# 	n = int(input())
# 	graph = []
# 	for _ in range(n):
# 		graph.append(list(map(int, input().split())))
# 	fishs = []

# 	time = 0
# 	fish_length = 2
# 	while True:
# 		for i in range(n):
# 			for j in range(n):
# 				if graph[i][j] != 0:
# 					if graph[i][j] == 9:
# 						sark = [i, j]
# 					elif graph[i][j] < fish_length:
# 						fishs.append([i, j])

# 		# 더 먹을 수 있는 물고기 없으면 종료
# 		if len(fishs) == 0:
# 			break
# 		min_fish_pos = [] # 최소 물고기 위치들
# 		for fish in fishs:
# 			tmp_dis = distance(sark, fish)
# 			if tmp_dis < min_dis:
# 				min_dis = tmp_dis # 최소 길이
# 				min_fish_pos = [fish] # 최소 물고기 위치 초기화
# 			elif tmp_dis == min_dis:
# 				min_fish_pos.append(fish) # 같은 길이에 물고기가 있으면 위치에 추가

# 		min_pos = []
# 		min_len = 0
# 		if len(min_fish_pos) == 1:
# 			min_len = distance(sark, min_fish_pos[0]) # 시간 추가
# 			min_pos = min_fish_pos[0]
# 		elif len(min_fish_pos) > 1:
# 			tmp = 0
# 			for fish in fishs:
# 				if fish[0] < sark[0]:
# 					if tmp != 0:

# 	print(time)

# solution()