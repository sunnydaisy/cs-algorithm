# 탑승구

"""

4
3
4
1
1
result : 2


4
6
2
2
3
3
4
4
result : 3

"""

import sys

input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def soluton():
    g = int(input())
    p = int(input())
    parent = [i for i in range(g + 1)]
    gates = []
    time = 0
    for _ in range(p):
        gates.append(int(input()))
    for gate in gates:
        if find_parent(parent, gate) != 0:
            union_parent(parent, parent[gate] - 1, parent[gate])
        else:
            break
        time += 1
    print(time)
    return 0

soluton()