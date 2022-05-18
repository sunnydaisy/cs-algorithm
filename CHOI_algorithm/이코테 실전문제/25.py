# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
	diff = [[i, 0] for i in range(N + 1)]
	diff[0][1] = -1e9
	for level in range(1, N + 1):
		reach_num = 0
		stuck_num = 0
		for stg in stages:
			if stg >= level:
				reach_num += 1
				if stg == level:
					stuck_num += 1
		if reach_num == 0:
			diff[level][1] = 0
		else:
			diff[level][1] = (stuck_num / reach_num)
	diff.sort(key=lambda x : (-x[1], x[0]))
	answer = [i[0] for i in diff]
	answer = answer[:-1]
	return answer
	
solution(4,	[4,4,4,4,4])