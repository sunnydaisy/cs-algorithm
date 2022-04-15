# 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061


def possible(answer):
	for x, y, stuff in answer:
		if stuff == 0: # 기둥인 경우 (바닥인경우, 아래에 기둥이 있는 경우, 왼쪽에 보가 있는 경우, 본인 자리에 보가 있는 경우 )
			if y == 0 or [x, y - 1 , 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer:
				continue
			return False
		else:			# 보인경우 (밑에 기둥이 있는 경우, 오른쪽 아래가 기둥인경우, 왼쪽과 오른쪽이 보인 경우)
			if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y , 1] in answer and [x + 1, y, 1] in answer):
				continue
			return False
	return True


def solution(n, build_frame):
	answer = []
	for fram in build_frame:
		x, y, stuff, op = fram
		if op == 1: # 설치하는 경우
			answer.append([x, y, stuff]) # 일단 추가하고 가능한지 확인
			if not possible(answer):
				answer.remove([x, y, stuff])
		elif op == 0: # 제거하는 경우
			answer.remove([x, y, stuff]) # 일단 제거하고 가능한지 확인
			if not possible(answer):
				answer.append([x, y, stuff])
	answer.sort()
	return answer







#-------------------------- 시도 1 실패
# def make_ck(graph, work):
# 	x = work[0]
# 	y = work[1]
# 	stuff = work[2]
# 	if stuff == 1 : # 보를 설치하는 경우
# 		if y == 0: # 바닥이면 바로 False 리턴
# 			return False
# 		if graph[x][y - 1] == 0: # 아래가 기둥안 경우
# 			return True
# 		elif ((x > 0 and y > 0) and graph[x - 1][y - 1] == 0) or ((x < len(graph) and y > 0) and graph[x + 1][y - 1] == 0): # 왼쪽 아래 또는 오른쪽 아래가 기둥인 경우
# 			return True
# 		elif x > 0 and graph[x - 1][y] == 1 and graph[x + 1][y] == 1 :# 왼쪽과 오른쪽이 보인 경우
# 			return True
# 	elif stuff == 0: # 기둥을 설치하는 경우
# 		if y == len(graph): # 꼭대기이면 바로 False 리턴
# 			return False
# 		if y == 0: 						# 바닥에 설치하는 경우 
# 			return True
# 		elif graph[x][y - 1] == 0: 		# 아래가 기둥인 경우
# 			return True
# 		elif graph[x - 1][y - 1] == 0 or graph[x + 1][y - 1] == 0: # 보의 한쪽 끝인경우
# 			return True
# 	return False


# def solution(n, build_frame):
# 	graph = [[-1]* (n + 1) for _ in range(n + 1)]
# 	for work in build_frame:
# 		x = work[0]
# 		y = work[1]
# 		stuff = work[2]
# 		build = work[3]
# 		if make_ck(graph, work): # 설치 가능한 경우
# 			if build == 1: # 설치 하려는 경우
# 				if stuff == 0: # 기둥인 경우
# 					graph[x][y] = 0
# 				elif stuff == 1: # 보인 경우
# 					graph[x][y] = 1
# 			else : # 철거 하려는 경우
# 				graph[x][y] = -1
# 	return



n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))