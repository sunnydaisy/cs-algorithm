# 화성 탐사

"""

3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

"""

import sys
from collections import deque

input = sys.stdin.readline
INF = 1e9
def solution():
    t = int(input())
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for _ in range(t):
        n = int(input())
        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split())))
        new_graph = []
        for _ in range(n):
            new_graph.append([INF] * n)
        q = deque()
        q.append((0, 0))
        new_graph[0][0] = graph[0][0]
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if new_graph[nx][ny] <= new_graph[x][y] + graph[nx][ny]:
                    continue
                new_graph[nx][ny] = new_graph[x][y] + graph[nx][ny]
                q.append((nx, ny))
        print(new_graph[n - 1][n - 1])

solution()