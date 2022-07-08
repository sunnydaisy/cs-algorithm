def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i] == False:
            dfs(computers, i, visited)
            answer += 1

    return answer


def dfs(graph, i, visited):
    visited[i] = True
    # print(i, graph[i])
    print()
    for j in graph[i]:
        print(i, j, graph[i])
        if visited[j] == False:
            dfs(graph, j, visited)

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# ------------------------------------- 실패 : 테케 9번만 실패
# def find_parent(parent, a):
#     if parent[a] != a:
#         parent[a] = find_parent(parent, parent[a])
#     return parent[a]
    
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def solution(n, computers):
#     answer = 0
#     parent = [i for i in range(n + 1)]
    
#     for i in range(len(computers)):
#         for j in range(len(computers[i])):
#             if computers[i][j] == 1:
#                 union_parent(parent, i, j)
#     # print(parent)
#     return len(set(parent)) - 1

