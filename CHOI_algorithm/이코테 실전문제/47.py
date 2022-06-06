# 청소년 상어
# https://www.acmicpc.net/problem/19236

import sys

input = sys.stdin.readline
n = 4
INF = int(1e9)
def fish_move(graph):
	min_num, min_pos = INF, [INF, INF]
	for i in range(n):
		for j in range(n):
			if min_num > graph[i][j]:
				min_num = graph[i][j]
				min_pos = [i, j]
	


def shark_move(graph, shark_pos):
	return [s_x, s_y]

def solution():
	graph = [[] for _ in range(n)]
	for j in range(n):
		tmp = list(map(int, input().split()))
		for i in range(0, len(tmp), 2):
			graph[j].append([tmp[i], tmp[i + 1]])
	shark_pos = [0, 0]
	# 0,0 물고기 먹는 코드 필요
	while True:
		fish_move(graph)
		shark_pos = shark_move(graph, shark_pos)


solution()