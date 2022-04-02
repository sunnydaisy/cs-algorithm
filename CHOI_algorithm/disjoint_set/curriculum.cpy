from collections import deque

n = int(input())
indegree = [0] * (n + 1)
graph = [[]for _ in range(n + 1)]

max_cost = [(0,0)] # (해당 노드 비용, 지금 노드까지 오는 비용)

for node in range(1, n + 1):
	line = list(map(int, input().split()))
	# max_cost[node][0] = int(line[0])
	max_cost.append([line[0], 0])
	for i in range(len(line)):
		if i == 0:
			continue
		elif line[i] == -1:
			break
		else:
			graph[line[i]].append(node)
			indegree[node] += 1

def topology():
	q = deque()
	result = [0] * (n + 1)
	
	for i in range(1, n + 1):
		if indegree[i] == 0:
			q.append(i)
	
	while q:
		now = q.popleft()
		for i in graph[now]:
			indegree[i] -= 1
			max_cost[i][1] = max(max_cost[i][1], sum(max_cost[now]))
			if indegree[i] == 0:
				q.append(i)
		result[now] = sum(max_cost[now])
	
	for i in range(1, n + 1):
		print(result[i])

topology()