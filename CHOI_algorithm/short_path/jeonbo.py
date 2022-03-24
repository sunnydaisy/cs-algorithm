import sys
import heapq


INF = int(1e9)
input = sys.stdin.readline

n ,m ,c = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[]] * (n + 1)

for _ in range(m):
	x, y, z = map(int, input().split())
	graph[x].append((z, y)) # cost , city

def dijstra(start):
	distance[start] = 0
	q = []
	heapq.heappush(q, (0, start))
	while q:
		dis, city = heapq.heappop(q)
		if distance[city] < dis:
			continue
		for i in graph[city]:
			cost = dis + i[0]
			if cost < distance[i[1]]:
				distance[i[1]] = cost
				heapq.heappush(q, (cost, i[1]))

dijstra(c)

count = 0
max_num = 0
for i in distance:
	if i < INF and i != 0:
		count += 1
		max_num = max(max_num, i)

print(count, max_num)