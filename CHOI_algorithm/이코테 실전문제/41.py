# 여행 계획

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3


"""

import sys

input = sys.stdin.readline

def find_parents(parents, a):
    if parents[a] != a:
        parents[a] = find_parents(parents, parents[a])
    return parents[a]

def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution():
    n, m = map(int, input().split())
    parnets = [i for i in range(n + 1)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] == 1:
                union_parents(parnets, i+1, j+1)

    paths = list(map(int, input().split()))
    # for i in range(len(paths)):
    #     if i == 0:
    #         ck = parnets[paths[i]]
    #     else:
    #         if parnets[paths[i]] != ck:
    #             print("NO")
    #             return -1
    # print("YES")
    for i in range(m - 1):
        if find_parents(parnets, i) != find_parents(parnets, i + 1):
            print("NO")
            return -1
    print("YES")
    return 0


solution()