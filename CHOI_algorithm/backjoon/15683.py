import sys

input = sys.stdin.readline
graph = []

def solution():
    n, m = map(int, input().split())
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    # cctv 초기화 (번호, x, y)
    cctv = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                cctv.append([graph[x][y], x, y])

    
    print(graph)

# def dfs():
    

# solution()