# 금광

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

"""



# ----------------------------------------- 해설 : 이 방식이 더 효율적일 듯
for tc in range(int(input())):
	n, m = map(int, input().split())
	array = list(map(int, input().split()))

	dp = []
	index = 0
	for i in range(n):
		dp.append(array[index : index + m])
		index += m
	for j in range(1, m):
		for i in range(n):
			 # 왼쪽 위
			if i == 0:
				left_up = 0
			else:
				left_up = dp[i - 1][j - 1]
			# 왼쪽 아래
			if i == n - 1: 
				left_down = 0
			else:
				left_down = dp[i + 1][j - 1]
			# 왼쪽에서 오는 경우
			left = dp[i][j - 1] 
			dp[i][j] = dp[i][j] + max(left, left_down, left_up)
	result = 0
	for i in range(n):
		result = max(result, dp[i][m - 1])
	print(result)
	


# ------------------------------ 2회차 시도 후 정답인듯?
# import sys
# from collections import deque

# def bfs(graph):
# 	q = deque()
# 	n = len(graph)
# 	m = len(graph[0])
# 	for i in range(len(graph)):
# 		q.append((i, 0, 0))
# 	answer = 0
# 	while q:
# 		dx, dy, tmp = q.popleft()
# 		if dx < 0 or dy < 0 or dx >= n or dy >= m:
# 			answer = max(answer, tmp)
# 			continue
# 		tmp += graph[dx][dy]
# 		q.append((dx + 1, dy + 1 , tmp))
# 		q.append((dx - 1, dy + 1 , tmp))
# 		q.append((dx, dy + 1 , tmp))
# 	return answer



# def solution():
# 	t = int(input())

# 	while t > 0:
# 		n, m =  map(int, input().split())
# 		graph = []
# 		arr = list(map(int, sys.stdin.readline().split()))
# 		for i in range(0, len(arr), m):
# 			graph.append(arr[i : i + m])
# 		print(bfs(graph))
# 		t -= 1
# solution()