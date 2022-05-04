# 인구 이동
# https://www.acmicpc.net/problem/16234


# ---------------------------------- 해설
# import sys
# from collections import deque

# n, l, r = map(int, input().split())

# graph = []
# for _ in range(n):
# 	graph.append(list(map(int, sys.stdin.readline().split())))

# def bfs(open_graph, x, y, index):
# 	united = []
# 	united.append((x, y))
# 	dx = [-1, 0, 1, 0]
# 	dy = [0, 1, 0, -1]
# 	q = deque()
# 	q.append((x, y))
# 	open_graph[x][y] = index
# 	sum_tmp = graph[x][y] # 인수 수
# 	count = 1
# 	while q:
# 		x, y = q.popleft()
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if 0 <= nx < n and 0 <= ny < n and open_graph[nx][ny] == -1:
# 				if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
# 					q.append((nx, ny))
# 					sum_tmp += graph[nx][ny]
# 					count += 1
# 					open_graph[nx][ny] = index
# 					united.append((nx, ny))
# 	for i, j in united:
# 		graph[i][j] = sum_tmp // count

# def solution():
# 	day = 0
# 	while day <= 2001:
# 		open_graph = [[-1] * n for _ in range(n)]
# 		index = 0
# 		for i in range(n):
# 			for j in range(n):
# 				if open_graph[i][j] == -1:	# 방문한 적이 없는 경우
# 					bfs(open_graph, i, j, index)
# 					index += 1
# 		if index == n * n:
# 			break
# 		day += 1
# 	return day



# ------------------------------------ 그냥 BFS 로 해봤는데 테스트케이스는 통과했으나 정답이 아님
import sys
from collections import deque

n, l, r = map(int, input().split())

def bfs(graph, visited, x, y):
	q = deque()
	tmp = graph[x][y]	# 인구수 합
	count = 1	# 도시 개수
	q.append((x + 1, y, graph[x][y]))
	q.append((x - 1, y, graph[x][y]))
	q.append((x, y + 1, graph[x][y]))
	q.append((x, y - 1, graph[x][y]))
	change_list = [(x, y)]
	visited[x][y] = True
	while q:
		tx, ty, before = q.popleft()
		if tx < 0 or ty < 0 or tx >= n or ty >= n or visited[tx][ty] == True: # 방문했었거나 범위 벗어나는 경우
			continue
		if abs(graph[tx][ty] - before) < l or abs(graph[tx][ty] - before) > r: # 인구 차이가 조건에 성립하는 경우
			continue
		visited[tx][ty] = True		# 방문 표시
		change_list.append((tx, ty)) # 바꿀 좌표 추가
		tmp += graph[tx][ty]
		q.append((tx + 1, ty, graph[tx][ty]))
		q.append((tx - 1, ty, graph[tx][ty]))
		q.append((tx, ty + 1, graph[tx][ty]))
		q.append((tx, ty - 1, graph[tx][ty]))
		count += 1
	for tx, ty in change_list:
		graph[tx][ty] = int(tmp / count)
	return len(change_list)



def solution():
	graph = []
	for _ in range(n):
		graph.append(list(map(int, sys.stdin.readline().split())))
	day = 0
	while day <= 2000:
		visited = [[False] * n for _ in range(n)]
		flag = 0
		for i in range(n):
			for j in range(n):
				if visited[i][j] == False:	# 방문한 적이 없는 경우
					if bfs(graph, visited, i, j) > 1:
						flag = 1		# 이 부분에서 뭔가 잘못되어서 틀린듯
		if flag == 0:
			return day
		day += 1
	return day





# ----------------------------------------- 시도 1 : 실패
# def bfs(graph, x, y, visited, before):
# 	if x < 0 or y < 0 or x >= n or y >= n:
# 		return 0, 0
# 	if visited[x][y] == True:
# 		return 0, 0
# 	if l <= (graph[x][y] - before) and (graph[x][y] - before) <= r:
# 		tmp = graph[x][y]
# 		visited[x][y] = True
# 		ct = 1
# 		result = bfs(graph, x + 1, y, visited, graph[x][y])
# 		tmp += int(result[0])
# 		ct += result[1]
# 		result = bfs(graph, x - 1, y, visited, graph[x][y])
# 		tmp += result[0]
# 		ct += result[1]
# 		result = bfs(graph, x, y + 1, visited, graph[x][y])
# 		tmp += result[0]
# 		ct += result[1]
# 		result = bfs(graph, x, y - 1, visited, graph[x][y])
# 		tmp += result[0]
# 		ct += result[1]
# 		return (tmp, ct)
# 	return 0, 0

# def op(graph):
# 	visited = [[False] * n for _ in range(n)]
# 	for i in range(n):
# 		for j in range(n):
# 			tmp, ct = bfs(graph, i, j, visited, graph[i][j])
# 			if ct > 1: # 인접한게 있었을 때
# 				for rx in range(n):
# 					for ry in range(n):
# 						if visited[rx][ry] == True:
# 							graph[rx][ry] = int(tmp / ct)
# 							visited[rx][ry] = False
# 				return ct

# def solution():
# 	graph = []
# 	for _ in range(n):
# 		graph.append(list(map(int, sys.stdin.readline().split())))
# 	visited = [[False] * n for _ in range(n)]
# 	count = 1
# 	final = n * n
# 	while count <= 2000:
# 		if op(graph) == final:
# 			return count
# 		count += 1
# 	return 0



print(solution())