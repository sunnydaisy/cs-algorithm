# 어두운 길

"""

7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11


"""
import time
# ------------------------------ 풀이 1 : 배열 사용 (0.005545ms)

# import sys

# input = sys.stdin.readline

# def find_parent(parent, a):
#     if parent[a] != a:
#         parent[a] = find_parent(parent, parent[a])
#     return parent[a]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if  a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# def solution():
#     n, m = map(int, input().split())
#     start = time.time()
#     parent = [i for i in range(n)]
#     edges = []
#     for _ in range(m):
#         a, b, cost = map(int, input().split())
#         edges.append((cost, a, b))
#     result = 0
#     whole_cost = 0
#     edges.sort()
#     for edge in edges:
#         cost, a, b = edge
#         whole_cost += cost
#         if find_parent(parent, a) != find_parent(parent, b):
#             union_parent(parent, a, b)
#             result += cost
#     print(whole_cost - result)
#     print(time.time() - start)


# solution()


# ------------------------------- 풀이 2 : 힙큐 사용 (0.0059ms)
import heapq
import sys

input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if  a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution():
    n, m = map(int, input().split())
    start = time.time()
    parent = [i for i in range(n)]
    q = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        heapq.heappush(q, (cost, a, b))
    result = 0
    while q:
        cost, a, b = heapq.heappop(q)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print(cost)
    print(time.time() - start)

solution()