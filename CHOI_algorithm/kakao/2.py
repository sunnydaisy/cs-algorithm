def find_idx(queue1, queue2):
	n = len(queue1)
	target = (sum(queue1) + sum(queue2)) // 2
	que = queue1 + queue2 + queue1
	pivot_len = len(queue1) + len(queue2) - 1
	while pivot_len > 0:
		for i in range(len(queue1) + len(queue2)):
			if sum( que[i: i + pivot_len]) == target:
				return i, pivot_len
			
		pivot_len -= 1

def solution(queue1, queue2):
	find_idx(queue1, queue2)
	return -1, -1






# ---------------------------------------------- 2회차 시간초과
# def binary_search(array, target, start, end):
# 	if start > end:
# 		return
# 	mid = (end + start) // 2
# 	if array[start:mid] == target:
# 		return start, mid
# 	elif array[start:mid] > target:
# 		return binary_search(array, target, start, mid - 1)
# 	else:
# 		return binary_search(array, target, start, mid + mid // 2)

# def put_index(queue1, queue2):
# 	que = queue1 + queue2 + queue1
# 	sum_1 = sum(queue1)
# 	sum_2 = sum(queue2)
# 	target = (sum_1 + sum_2) // 2
# 	n = len(que)

	
# 	for i in range(len(queue1) + len(queue2)):
# 		tmp = 0
# 		for j in range(i, n):
# 			tmp += que[j]
# 			if tmp > target:
# 				break
# 			elif tmp == target:
# 				return i, j
# 	return -1 ,-1


# def solution(queue1, queue2):
# 	qu1_len = len(queue1)
# 	qu2_len = len(queue2)
# 	a, b = put_index(queue1, queue2)
# 	if a < 0 or b < 0:
# 		return -1
# 	if a < qu1_len and b < qu1_len: # 1 , 1 에 있는 경우
# 		if b == qu1_len - 1: # 끝에 닿은 경우
# 			return a
# 		else: # 중간에 끊긴 경우
# 			return b + qu2_len
# 	elif a < qu1_len and  qu1_len <= b < qu1_len + qu2_len: # 1, 2
# 		if b == qu1_len + qu2_len - 1: # 2 끝에 닿은 경우
# 			return b
# 		else:
# 			return b - qu1_len + a + 1
# 	elif qu1_len <= a < qu1_len + qu2_len and qu1_len <= b < qu1_len + qu2_len: # 2, 2
# 		return b - qu1_len + a + 1
# 	elif qu1_len <= a < qu1_len + qu2_len and qu1_len + qu2_len <= b: # 2, 3
# 		return a +  b - qu1_len


# [*,a,*,b,*]
# [*,*,a,*,b]
# [*,*,a,*], [b,*]
# [*,*,a,*], [*, b,*]
# [*,*,a,*], [*,b]







solution([1, 2, 1, 2], [1, 10, 1, 2])

# ------------------------------- 1회차 : 시간초과
# from collections import deque

# def switch (des, src):
# 	des.append(src.popleft())


# def solution(queue1, queue2):
# 	# target = (sum(queue1) + sum(queue2)) // 2
# 	if (sum(queue1) + sum(queue2)) % 2 == 1:
# 		return -1 
# 	que1 = deque(queue1)
# 	que2 = deque(queue2)
# 	answer = 0
# 	while sum(que1) != sum(que2):
# 		if sum(que1) > sum(que2):
# 			que2.append(que1.popleft())
# 		else:
# 			que1.append(que2.popleft())
# 		answer += 1
# 		if answer > 600000:
# 			return -1
# 	return answer