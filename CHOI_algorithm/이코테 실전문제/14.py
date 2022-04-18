# 외벽 검사
# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations

def solution(n, weak, dist):
	length = len(weak)
	for i in range(length):
		weak.append(weak[i] + n)
	result = len(dist) + 1
	for friedns in list(permutations(dist, len(dist))): # 친구 정렬 경우의 수
		for start in range(length): # 시작 인덱스
			count = 1 # 친구 수
			position = weak[start] + friedns[count - 1] # 친구가 갈 수 있는 최대 위치
			for index in range(start, start + length): # 시작 인덱스 부터 마지막 결함 인덱스 까지
				if position < weak[index]: # 친구가 갈 수 있는 최대 범위를 넘었은 경우
					count += 1
					if count > len(dist):
						break
					position = weak[index] + friedns[count - 1]
			result = min(result, count)
	if result > len(dist):
		return -1
	return result




# ---------------------------------- 해설
# from itertools import permutations

# def solution(n, weak, dist):
# 	length = len(weak)
# 	for i in range(length):
# 		weak.append(weak[i] + n)
# 	answer = len(dist) + 1
# 	for start in range(length):
# 		for friends in list(permutations(dist, len(dist))):
# 			count = 1 # 투입할 친구의 수
# 			position = weak[start] + friends[count - 1] # 해당 친구가 점검할 수있는 마지막 위치
# 			for index in range(start, start + length):
# 				if position < weak[index]: # 점검할 수 있는 위치를 벗어나는 경우
# 					count += 1
# 					if count > len(dist): # 더 투입이 불가능한 경우
# 						break
# 					position = weak[index] + friends[count - 1]
# 			answer = min(answer, count)
# 	if answer > len(dist):
# 		return -1
# 	return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n, weak, dist))