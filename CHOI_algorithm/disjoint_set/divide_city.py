# 도시 분할 계획

# 답
import sys

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a

def op():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    parent = [i for i in range(n + 1)]
    graph = []
    result = 0
    max_len = 0
    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph.append((cost, a, b))
    graph.sort()
    for cost, a, b in graph:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            max_len = cost
            result += cost
    print(result - max_len)

op()


# 시도 2
# 전체적으로 답과 거의 똑같은데 밑에 set 를 사용한 부분에서 시간복잡도가 올라가서 틀렸다. 이럴 필요 없이 단순히 크루스칼 알고리즘을 \ 
# 사용한 뒤에 마지막으로 들어오는 가장 값이 큰 cost 를 result 에서 빼주면 된다. 가장 큰 길만 빼주면 마을이 2개가 되고 가장 적은 코스트로 마을을 나누게 된다.
# import sys

# def find_parent(parent, a):
#     if parent[a] != a:
#         parent[a] = find_parent(parent, parent[a])
#     return parent[a]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a > b :
#         parent[a] = b
#     else:
#         parent[b] = a

# def op():
#     input = sys.stdin.readline
#     n, m = map(int, input().split())

#     parent = [i for i in range(n + 1)]
#     graph = []
#     result = 0
#     for _ in range(m):
#         a, b, cost = map(int, input().split())
#         graph.append((cost, a, b))
#         # graph[a].append((cost, b))
#     graph.sort()
#     for cost, a, b in graph:
#         if len(set(parent[1:])) == 2: # 이 부분 때문에 시간 복잡도가 올라가서 틀림
#             break
#         if find_parent(parent, a) != find_parent(parent, b):
#             union_parent(parent, a, b)
#             result += cost
#     print(result)

# op()






# 시도 1 
# 1개의 신장트리만 만들었다

# n, m = map(int, input().split())

# parent = [i for i in range(n + 1)]
# # graph = [[] for _ in range(n + 1)]
# graph = []

# def find_parent(parent, a):
#     if parent[a] != a:
#         parent[a] = find_parent(parent, parent[a])
#     return parent[a]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a > b :
#         parent[a] = b
#     else:
#         parent[b] = a

# def op():
#     result = 0
#     for _ in range(m):
#         a, b, cost = map(int, input().split())
#         graph.append((cost, a, b))
#         # graph[a].append((cost, b))
#     graph.sort()
#     for cost, a, b in graph:
#         if find_parent(parent, a) != find_parent(parent, b):
#             union_parent(parent, a, b)
#             result += cost
#     print(result)
# op()