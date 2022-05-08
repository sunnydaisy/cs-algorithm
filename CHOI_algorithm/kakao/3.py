from collections import deque

def solve_count(alp, cop, problems):
	for pro in problems:
		if alp < pro[0]:
			return False
		elif cop < pro[1]:
			return False
	return True

def bfs(alp, cop, problems):
	q = deque()
	q.append([alp, cop, 0])
	result = 1e9
	while q:
		na, nc, time = q.popleft()
		if time > result:
			continue
		if solve_count(na, nc, problems):
			result = min(time, result)
			continue
		q.append([na + 1, nc, time + 1])
		q.append([na, nc + 1, time + 1])
		for pro in problems:
			alp_req, cop_req, alp_rwd, cop_rwd, cost = pro
			if na >= alp_req and nc >= cop_req:
				q.append([na + alp_rwd, nc + cop_rwd, time + cost])
	return result


def solution(alp, cop, problems):
	return bfs(alp, cop, problems)







# ------------------------------------- 3회차 : 시간초과 : 힙으로 바꿔봤는데 시간초과임
# import heapq

# def solve_count(alp, cop, problems):
# 	for pro in problems:
# 		if alp < pro[0]:
# 			return False
# 		elif cop < pro[1]:
# 			return False
# 	return True

# def bfs(alp, cop, problems):
# 	q = []
# 	heapq.heappush(q, [0, alp, cop])
# 	result = 1e9
# 	while q:
# 		time, na, nc = heapq.heappop(q)
# 		if time > result:
# 			return result
# 		if solve_count(na, nc, problems):
# 			result = min(time, result)
# 			continue
# 		heapq.heappush(q, [time + 1, na + 1, nc])
# 		heapq.heappush(q, [time + 1, na, nc + 1])
# 		for pro in problems:
# 			alp_req, cop_req, alp_rwd, cop_rwd, cost = pro
# 			if na >= alp_req and nc >= cop_req:
# 				heapq.heappush(q, [time + cost, na + alp_rwd, nc + cop_rwd])
# 	return result


# def solution(alp, cop, problems):
# 	return bfs(alp, cop, problems)






# from collections import deque

# def cost_cal(practice, na, nc, n_time, req_alp, req_cop):
# 	t_alp, t_cop , cost = practice
# 	if t_alp == 0:
# 		(req_alp - na) / t_alp
# 	while na < req_alp or nc < req_cop:
# 		na += t_alp 
# 		nc += t_cop
# 		n_time += cost
# 	return [na, nc, n_time]

# def solve_count(alp, cop, problems):
# 	for pro in problems:
# 		if alp < pro[0]:
# 			return False
# 		elif cop < pro[1]:
# 			return False
# 	return True

# def bfs(alp, cop, problems):
# 	q = deque()
# 	q.append([alp, cop, 0])
# 	result = 1e9
# 	practice = [[1, 0, 1], [0, 1, 1]]
# 	while q:
# 		na, nc, time = q.popleft()
# 		if time > result:
# 			continue
# 		if solve_count(na, nc, problems):
# 			result = min(time, result)
# 			continue
# 		for pro in problems:
# 			alp_req, cop_req, alp_rwd, cop_rwd, cost = pro
# 			if na >= alp_req and nc >= cop_req:
# 				if [alp_rwd, cop_rwd, cost] not in practice:
# 					practice.append([alp_rwd, cop_rwd, cost])
# 			if na < alp_req or nc < cop_req:
# 				for prac in practice:
# 					q.append(cost_cal(prac, na, nc, time, alp_req, cop_req))
				
# 	return result


# def solution(alp, cop, problems):
# 	return bfs(alp, cop, problems)
	




# ------------------------------ 시도 2 : 정확성 통과, 효율성 탈락
# import heapq
# from collections import deque

# def solve_count(alp, cop, problems):
# 	for pro in problems:
# 		if alp < pro[0]:
# 			return False
# 		elif cop < pro[1]:
# 			return False
# 	return True

# def bfs(alp, cop, problems):
# 	q = deque()
# 	q.append([alp, cop, 0])
# 	result = 1e9
# 	while q:
# 		na, nc, time = q.popleft()
# 		if time > result:
# 			continue
# 		if solve_count(na, nc, problems):
# 			result = min(time, result)
# 			continue
# 		q.append([na + 1, nc, time + 1])
# 		q.append([na, nc + 1, time + 1])
# 		for pro in problems:
# 			alp_req, cop_req, alp_rwd, cop_rwd, cost = pro
# 			if na >= alp_req and nc >= cop_req:
# 				q.append([na + alp_rwd, nc + cop_rwd, time + cost])
# 	return result


# def solution(alp, cop, problems):
# 	return bfs(alp, cop, problems)



# ------------------------------------ dfs 시도 실패
#  def solve_count(alp, cop, problems):
# 	for pro in problems:
# 		if alp < pro[0]:
# 			return False
# 		elif cop < pro[1]:
# 			return False
# 	return True

# def dfs(alp, cop, problems, time):
# 	if solve_count(alp, cop, problems):
# 		return time
# 	result = 1e9
# 	result = min(dfs(alp + 1, cop, problems, time + 1), result)
# 	result = min(dfs(alp, cop + 1, problems, time + 1), result)
# 	for pro in problems:
# 		alp_req, cop_req, alp_rwd, cop_rwd, cost = pro
# 		if alp >= alp_req and cop >= cop_req:
# 			result = min(dfs(alp + alp_rwd, cop + cop_rwd, problems, time + cost), result)
# 	return result

# def solution(alp, cop, problems):
# 	answer = dfs(alp, cop, problems, 0)
# 	return answer

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]] 
solution(alp, cop, problems)