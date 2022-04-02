# 팀 결성

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

def find_parent(parent, a):
    if parent[a] != a:
        # return find_parent(parent, parent[a]) -- 틀림
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def op():
    result = []
    for _ in range(m):
        ck, a, b = map(int, input().split())
        if ck == 0:
            # 팀 합치기
            union_parent(parent, a, b)
        elif ck == 1:
            # 같은 팀 확인
            if find_parent(parent, a) != find_parent(parent, b):
                result.append(0)
            else:
                result.append(1)
    for i in result:
        if i == 0:
            print("NO")
        else:
            print("YES")
op()