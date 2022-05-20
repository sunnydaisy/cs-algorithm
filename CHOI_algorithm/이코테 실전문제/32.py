# 정수 삼각형
# https://www.acmicpc.net/problem/1932

# ----------------------------------------- 성공 : 해설과 똑같이 구현
def solution():
    n = int(input())
    graph = []
    for i in range(n):
        arr = list(map(int, input().split()))
        while len(arr) < n:
            arr.append(0)
        graph.append(arr)
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                left = 0
            else:
                left = graph[i - 1][j - 1]
            if j == n - 1:
                right = 0
            else:
                right = graph[i - 1][j]
            graph[i][j] = graph[i][j] + max(left, right)
        # if i == 0:
        #     tmp = arr[0]
        #     continue
    print(max(graph[n - 1]))


solution()