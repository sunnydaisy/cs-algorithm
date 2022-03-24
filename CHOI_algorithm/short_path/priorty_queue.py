from dis import dis
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())
# 각 노드에 연결되어 있는 노드에 대하 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
	a, b, c = map(int, input().split())
	# a 노드에서 b 로 가는 비용이 c 라는 의미
	graph[a].append((b, c))

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q:
		dist, now = heapq.heappop(q) # dist 는 시작노드에서 now 노드까지의 거리
		if distance[now] < dist:
			continue
		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
	if distance[i] == INF:
		print("INFINITY")
	else:
		print(distance[i])