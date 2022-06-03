# 행성 터널
# https://www.acmicpc.net/problem/2887

# ------------------------------------- 해설 : x, y, z 에 대해서 따로 생각하고 정렬한뒤 배열 앞뒤 사이의 간격이 최소 간격이 된다는 개념을 못잡았음
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

def solution():
	n = int(input())
	x = []
	y = []
	z = []
	parent = [i for i in range(n)]
	for i in range(n):
		a, b, c = map(int, input().split())
		x.append((a, i))
		y.append((b, i))
		z.append((c, i))
	x.sort()
	y.sort()
	z.sort()
	edges = []
	for i in range(n - 1):
		edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
		edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
		edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))
	edges.sort()
	result = 0
	for edge in edges:
		cost, a, b = edge
		if find_parent(parent, a) != find_parent(parent, b):
			union_parent(parent, a, b)
			result += cost
	print(result)
solution()


# --------------------------------------- 1 회차 : 메모리 초과 (n^2 이여서 그런듯)
# import heapq
# import sys

# input = sys.stdin.readline

# def distanse(planet, a, b):
# 	x = abs(planet[a][0] - planet[b][0])
# 	y = abs(planet[a][1] - planet[b][1])
# 	z = abs(planet[a][2] - planet[b][2])
# 	return min(x, y, z)

# def find_parent(parent, a):
# 	if parent[a] != a:
# 		parent[a] = find_parent(parent, parent[a])
# 	return parent[a]

# def union_parent(parent, a, b):
# 	a = find_parent(parent, a)
# 	b = find_parent(parent, b)
# 	if a < b:
# 		parent[b] = a
# 	else:
# 		parent[a] = b

# def solution():
# 	n = int(input())
# 	planet = []
# 	for _ in range(n):
# 		planet.append(tuple(map(int, input().split())))
# 	parent = [i for i in range(n)]
# 	q = []
# 	for i in range(n):
# 		for j in range(n):
# 			if i != j:
# 				heapq.heappush(q, (distanse(planet, i, j), i, j))
# 	result = 0
# 	while q:
# 		cost, a, b = heapq.heappop(q)
# 		if find_parent(parent, a) != find_parent(parent, b):
# 			union_parent(parent, a, b)
# 			result += cost
# 	print(result)
# solution()