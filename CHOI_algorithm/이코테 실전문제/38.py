# 정확한 순위

"""

6 6
1 5
3 4
4 2
4 6
5 2
5 4

"""

import sys
input = sys.stdin.readline

def solution():
	INF = 1e9
	n, m = map(int, input().split())
	graph = [[INF] * (n + 1) for _ in range(n + 1)]

	for _ in range(m):
		a, b = map(int, input().split())
		graph[a][b] = 1

	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if i == j:
				graph[i][j] = 0

	for k in range(1, n + 1):
		for i in range(1, n + 1):
			for j in range(1, n + 1):
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

	result = 0
	for i in range(1, n + 1):
		tmp = 0
		for j in range(1, n + 1):
			# if i != j and graph[i][j] == INF:
			# 	continue
			# tmp += 1
			if graph[i][j] != INF or graph[j][i] != INF:
				tmp += 1
		if tmp == n:
			result += 1
	print(result)
solution()

# ------------------------------------- 시도 2 : 다른 방식의 플로이드 방법도 실패

# def solution():
# 	n, m = map(int, input().split())
# 	graph = [[False] * (n + 1) for _ in range(n + 1)]
# 	rank = [0] * (n + 1)
# 	result = 0

# 	for _ in range(m):
# 		a, b = map(int, input().split())
# 		graph[a][b] = True
# 		# graph[b][a] = True

# 	for k in range(1, n + 1):
# 		for i in range(1, n + 1):
# 			for j in range(1, n + 1):
# 				if i != j and graph[i][k] == True and graph[k][j] == True:
# 					graph[i][j] = True

# 	for i in range(1, n + 1):
# 		count = 0
# 		for j in range(1, n + 1):
# 			if graph[i][j] == True:
# 				count += 1
# 		if count == n - 1:
# 			result += 1
# 	print(result)
# solution()




# ------------------------------------- 시도 1 : 실패 플로이드로 해봤는데 실패했다.
# def solution():
# 	INF = 1e9
# 	n, m = map(int, input().split())
# 	graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 	result = 0
# 	for _ in range(m):
# 		a, b = map(int, input().split())
# 		graph[a][b] = 1

# 	for k in range(1, n + 1):
# 		for i in range(1, n + 1):
# 			for j in range(1, n + 1):
# 				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 	for i in range(1, n + 1):
# 		tmp = 0
# 		for j in range(1, n + 1):
# 			if i != j and graph[i][j] == INF:
# 				continue
# 			tmp += 1
# 		if tmp == n:
# 			result += 1
# 	print(result)
# solution()