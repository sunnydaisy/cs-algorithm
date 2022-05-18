# 금광

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

"""
import sys

def bfs(graph, x, y):
	if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]):
		return -1
	tmp = graph[x][y]
	if y > len(graph[0]):
		return tmp
	return tmp + max(bfs(graph, x + 1, y + 1), bfs(graph, x, y + 1), bfs(graph, x - 1, y + 1))
	




def solution():
	t = int(input())

	while t > 0:
		n, m =  map(int, input().split())
		graph = []
		arr = list(map(int, sys.stdin.readline().split()))
		for i in range(0, len(arr), m):
			graph.append(arr[i : i + m])

		
		t -= 1
solution()