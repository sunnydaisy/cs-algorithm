n, m = map(int, input().split())
x, y, dir = map(int, input().split())

d = [[0] * m for _ in range(n)]
game_map = []
count = 1
check = [(0, -1), (-1, 0), (0, 1), (1, 0)]
flag = 0

for _ in range(n):
	game_map.append(list(map(int, input().split())))

d[x][y] = 1

while flag < 4:
	n_x = x + check[dir][0]
	n_y = y + check[dir][1]
	if game_map[n_x][n_y] == 0 and d[n_x][n_y] == 0:
		game_map[x][y] = 1
		d[n_x][n_y] = 1
		x = n_x
		y = n_y
		count += 1
		flag = -1
	if dir > 0:
		dir -= 1 
	else:
		dir = 3
	flag += 1
print(count)