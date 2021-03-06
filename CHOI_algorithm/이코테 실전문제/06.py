# 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891#

# 2회 차
# from collections import deque

# 정확성 (통과) // 효율성 (1개만 통과)
# def tr2_solution(food_times, k):
# 	INF = int(1e9)
# 	now = min(food_times)
# 	cnt = len(food_times)
# 	while (cnt != 0 and k // cnt >= now): # 도중에 하나 이상이 0이 되는 경우
# 		food_times = [i - now for i in food_times]
# 		k -= cnt * now
# 		now = INF
# 		cnt = 0
# 		for i in food_times:
# 			if i > 0:
# 				cnt += 1
# 				now = min(now, i)
# 	if cnt == 0:
# 		return -1
# 	if k // cnt > 0:
# 		food_times = [i - k // cnt for i in food_times]
# 		k %= cnt
# 	q = deque()
# 	for key, v in enumerate(food_times):
# 		if v > 0:
# 			q.append((key ,v))
# 	while q:
# 		ck = q.popleft()
# 		if k == 0:
# 			return ck[0] + 1
# 		if ck[1] > 0:
# 			q.append((ck[0], ck[1] - 1))
# 		k -= 1
# 	return -1



# def tr1_solution(food_times, k):
#     INT = int(1e9)
#     time = 0
#     count = len(food_times)
#     now = min(food_times)
#     while time + now * count < k:
#         time += now * count
#         tmp_arr = []
#         # for i in 
#         now = min(tmp_arr)
#         count = len(tmp_arr)

#     for i in range(len(food_times)):
#         food_times[i] -= now

#     q = deque()

#     for idx, value in enumerate(food_times):
#         if value > 0:
#             q.append((idx, value))

#     while time < k and q:
#         food = q.popleft()
#         time += 1
#         if food[1] == 1:
#             continue
#         q.append((food[0], food[1] - 1))

#     if time == k and q:
#         food = q.popleft()
#         return (food[0] + 1) 
#     else:
#         return (-1)







# 시도 1 (테스트케이스 : 실패)

# def solution(food_times, k):
# 	answer = 0
# 	idx = 0
# 	list = []
# 	food_ct = len(food_times)
# 	loop_ck = 0
# 	while len(list) <= k:
# 		if food_times[idx] > 0:
# 			list.append(idx)
# 			loop_ck = 0
# 		if idx >= food_ct - 1:
# 			idx = 0
# 			if loop_ck == 1:
# 				break
# 			loop_ck = 1
# 		idx += 1
# 	return list[k]


# 시도 2 (테스트케이스 : 통과 / 효율성 : 실패)
# 반복문을 많이 써서 효율성이 떨어지는 듯 하다.

# def solution(food_times, k):
# 	food_ct = len(food_times)
# 	ct = food_ct
# 	while ct > 0:
# 		if k + 1 > ct:
# 			for i in range(food_ct):
# 				if food_times[i] > 0:
# 					food_times[i] -= 1
# 		else:
# 			for i in range(food_ct):
# 				if food_times[i] > 0:
# 					k -= 1
# 					if k == -1:
# 						return i + 1
# 		k -= ct
# 		ct = food_ct - food_times.count(0)
# 	return -1


# 시도 3 (테스트케이스 : 통과 / 효율성 : 실패)
# 반복문 하나를 줄여서 효율성에 통과할 줄 알았는데 아니였다. 아마도 반복문을 이중 없이 써야하나보다.

# def solution(food_times, k):
# 	loop = 0
# 	food_ct = len(food_times)
# 	ct = food_ct
# 	while ct > 0:
# 		if k + 1 > ct:
# 			loop += 1
# 		else:
# 			for i in range(food_ct):
# 				if food_times[i] > loop:
# 					k -= 1
# 					if k == -1:
# 						return i + 1
# 		k -= ct
# 		ct = sum(i > loop for i in food_times)
# 	return -1


# 시도 4 (테스트케이스 : 실패 / 효율성 : 실패)
# 코드를 바꿔보려고 하다가 둘다 실패했다.

# def solution(food_times, k):
# 	loop = 0
# 	food_ct = len(food_times)
# 	ct = 0
# 	if k > len(food_times):
# 		loop = min(food_times)
# 		if sum(i > loop for i in food_times) == 0:
# 			loop -= 1
# 		ct = food_ct * loop
# 	for i in range(food_ct):
# 		if food_times[i] > loop:
# 			ct += 1
# 			if k + 1 == ct:
# 				return i + 1
# 	loop += 1
# 	for i in range(food_ct):
# 		if food_times[i] > loop:
# 			ct += 1
# 			if k + 1 == ct:
# 				return i + 1
# 	return -1

# 시도 5 (테스트케이스 : 실패 / 효율성 : 실패)
# 조건에 만족하는 요소의 개수만큼 더해서 k 보다 커지는 경우 종료하는 형식으로 하려고 했는데 역시 실패했다.

# def solution(food_times, k):
# 	loop = 0
# 	food_ct = len(food_times)
# 	# if k + 1 > food_ct:
# 	# 	loop = min(food_times)
# 	while True:
# 		tmp_ct = sum(i > loop + 1 for i in food_times)
# 		if tmp_ct == 0 :
# 			return -1
# 		if food_ct + tmp_ct > k + 1:
# 			loop += 1
# 			break
# 		food_ct += tmp_ct
# 		loop += 1
# 	for i in range(len(food_times)):
# 		if food_times[i] > loop:
# 			food_ct += 1
# 			if k + 1 == food_ct:
# 				return i + 1
# 	return -1


# import heapq

# def solution(food_times, k):
# 	if sum(food_times) <= k:
# 		return -1
	
# 	q = []
# 	for i in range(len(food_times)):
# 		heapq.heappush(q, (food_times[i], i + 1))
	
# 	length = len(food_times)
# 	past_time = 0

	

# food_times = [4,2,3,6,7,1,5,8]

# k = 16
# print(solution(food_times, k))


# 해설
import heapq

def solution(food_times, k):
	if sum(food_times) <= k:
		return -1

	q = [] # 큐
	for idx, value in enumerate(food_times):
		heapq.heappush(q, (value, idx + 1))  # (음식 시간, 음식 순서)
	
	previous = 0 # 마지막 음식 시간
	food_len = len(q) # 음식 개수
	while (q[0][0] - previous) * food_len <= k:
		now = heapq.heappop(q)[0]
		k -= (now - previous) * food_len
		food_len -= 1
		previous = now
	q.sort(key= lambda x : x[1])
	return q[k % food_len][1]
	



food_times = [100000000]
k = 99999999

print(solution(food_times, k))