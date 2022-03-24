INF = int(1e9)

# 노드의 개수, 간선의 개수
n = int(input())
m = int(input())

# 2차원 리스트 만들고 무한대로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
	for b in range(1, n + 1):
		if a == b:
			graph[a][b] = 0

# 각 선에 대한 정보 입력 받고, 그 값으로 초기화
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
	for b in range(1, n + 1):
		if graph[a][b] == INF:
			print('INF', end=' ')
		else:
			print(graph[a][b], end=' ')
	print()