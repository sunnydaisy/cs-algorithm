

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
	for b in range(1, n + 1):
		if a == b:
			graph[a][b] = 0

for _ in range(m):
	road = tuple(map(int, input().split()))
	graph[road[0]][road[1]] = 1
	graph[road[1]][road[0]] = 1

for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


x, k = map(int, input().split())
answer = graph[1][k] + graph[k][x]

if answer < INF:
	print(answer)
else:
	print(-1)


# import sys
# import heapq

# input = sys.stdin.readline
# n, m = map(int, input().split())
# INF = int(1e9)

# distance = [INF] * (n + 1)
# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
# 	f, t = map(int, input().split())
# 	graph[f].append((t, 1))

# def dijkstra(start):
# 	distance[start] = 0
# 	q = []
# 	heapq.heappush(q, (start, 0))
# 	while q:
# 		city, dis = heapq.heappop(q)
# 		if distance[city] < dis:
# 			continue
# 		for i in graph[city]:
# 			i[0] # 연결된 도시
# 			i[1] # 거리 비용 : 1
# 			cost =  dis + i[1]
# 			if cost < distance[i[0]]:
# 				distance[i[0]] = cost
# 				heapq.heappush(q, (i[0], cost))

# dijkstra(1)

# x , k = map(int, input().split())
# distance[k] 

