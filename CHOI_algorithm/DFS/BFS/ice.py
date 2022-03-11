# 음료수 얼려 먹기
# 답지를 한번 간단하게 보고 구현했다. 답지랑 똑같이 구현했더라..

n, m = map(int, input().split())

trace = []
for _ in range(n):
	trace.append(list(map(int, input())))

def dfs(x, y):
	if x <= -1 or y <= -1 or x >= n or y >= m:
		return False
	if trace[x][y] == 0:
		trace[x][y] = 1
		dfs(x - 1, y)
		dfs(x + 1, y)
		dfs(x, y + 1)
		dfs(x, y - 1)
		return True
	return False
	
count = 0

for i in range(n):
	for j in range(m):
		if dfs(i, j) == True:
			count += 1
print(count)
