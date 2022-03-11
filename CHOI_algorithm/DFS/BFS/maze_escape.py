
n, m = map(int, input().split())

maze = []
for _ in range(n):
	maze.append(list(map(int, input())))

# DFS 풀이
# count = 0

# visited = [[1] * m for _ in range(n)]
# ct_list = []

# def dfs(x, y, ct):
# 	if x <= -1 or y <= -1 or x >= n or y >= m or maze[x][y] == 0:
# 		return False
# 	if x == n - 1 and y == m - 1:
# 		ct_list.append(ct)
# 	maze[x][y] = 0
# 	dfs(x + 1, y, ct + 1)
# 	dfs(x - 1, y, ct + 1)
# 	dfs(x, y + 1, ct + 1)
# 	dfs(x, y - 1, ct + 1)

# dfs(0, 0, 1)
# print(min(ct_list))

from collections import deque


def bfs(n, m):
	queue = deque()
	queue.append([0, 0])
	except_list = []
	count = 2
	d_x = [1, 0, -1, 0]
	d_y = [0, 1, 0, -1]
	while queue:
		v = queue.popleft()
		x = v[0]
		y = v[1]
		for i in range(4):
			n_x = x + d_x[i]
			n_y = y + d_y[i]
			if n_x < 0 or n_x >= n or n_y < 0 or n_y >= m:
				continue
			if maze[n_x][n_y] != 1 or (n_x == 0 and n_y == 0):
				continue
			maze[n_x][n_y] = maze[x][y] + 1
			queue.append([n_x, n_y])


bfs(n, m)
# for i in maze:
# 	print(i)
print(maze[n - 1][m - 1])

