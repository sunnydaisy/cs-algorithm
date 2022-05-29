# 숨바꼭질

"""

6 7
3 6
4 3
3 2
1 3
1 2 
2 4
5 2

"""
# ----------------------------------- 
# 시도 1: 해결 (힙큐를 사용하므로 cost을 같이 넣어주는게 좋고, 마지막 출력 반복문은 인덱스를 사용해서 
# for i in range(1, n+1) 이런식으로하는게 좋을듯)
# ------------------------------------
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
def solution():
    start = 1
    n, m = map(int, input().split())
    distance = [INF] * (n + 1)
    distance[start] = 0
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1 # i 노드로 가는 비용는 dist + 1 이다. 왜냐하면 경로 비용은 다 1로 통일했다는 가정을 해서.
            if cost < distance[i]: # 이미 저장된 경로의 비용보다 더 적은 비용으로 갈 수 있으면
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    max_cost = 0
    max_idx = 0
    max_count = 0
    for idx, val in enumerate(distance):
        if val != INF:
            if val > max_cost:
                max_count = 1
                max_cost = val
                max_idx = idx
            elif val == max_cost:
                max_count += 1
    print(max_idx, max_cost, max_count)


solution()