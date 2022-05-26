# 플로이드
# https://www.acmicpc.net/problem/11404

import sys
INF = 1e9

def solution():
    n = int(input())
    m = int(input())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # for i in range(n + 1):
    #     for j in range(n + 1):
    #         if i == j:
    #             graph[i][j] = 0

    for _ in range(m):
        a, b, cost = map(int, sys.stdin.readline().split())
        graph[a][b] = min(cost, graph[a][b])
    
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF or a == b:
                print(0, end=' ')
            else:
                print(graph[a][b], end=' ')
        print()
    return


solution()