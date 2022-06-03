"""

6 4
1 4
2 3
2 4
5 6

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

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union_parents(parents, a, b)

print(parents)


