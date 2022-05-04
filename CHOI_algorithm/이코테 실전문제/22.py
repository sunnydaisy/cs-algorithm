# 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063

# ------------------------------- 해설 : set 를 활용할 생각을 못했다.
from collections import dequex

def get_next_pos(pos, board):
	able_pos = []
	pos = list(pos)
	pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	for i in range(4): # 상하좌우 갈 수 있는 경우 추가
		pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
		if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
			able_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
	if pos1_y == pos2_y: # 세로로 되어 있는 경우
		for i in [-1, 1]:
			if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: 
				able_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
				able_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
	elif pos1_x == pos2_x: # 가로로 되어 있는 경우
		for i in [-1, 1]:
			if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: 
				able_pos.append({(pos1_x, pos1_y), (pos1_x + i , pos1_y )})
				able_pos.append({(pos2_x, pos2_y), (pos2_x + i , pos2_y )})
	return able_pos




def solution(board):
	n = len(board)
	new_board = [[1] * (n + 2) for _ in range(n + 2)]
	for i in range(len(board)):
		for j in range(len(board)):
			new_board[i + 1][j + 1] = board[i][j]
	
	q = deque()
	pos = {(1, 1), (1, 2)}
	visited = []
	q.append((pos, 0))
	while q:
		pos, cost = q.popleft()
		if (n, n) in pos:	# 도착한 경우
			return cost
		# pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
		for next_pos in get_next_pos(pos, new_board):
			if next_pos not in visited: # 방문하지 않았던 곳이면
				q.append((next_pos, cost + 1))
				visited.append(next_pos)
	return -1


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))