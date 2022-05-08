import heapq

def dijkstra(start, graph, n):
	distance = [1e9] * (n + 1)
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q:
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))
	

def solution(n, paths, gates, summits):
	graph = [[] for _ in range(n + 1)]
	for path in paths:
		graph[path[0]].append(path[1:]) # 해당 노드에서 갈 수 있는 경로 추가 (경로, 비용)
	
	start = [1, 1e9] 

	answer = []
	return answer