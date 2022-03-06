# 무지의 먹방 라이브

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



def solution(food_times, k):
	loop = 0
	if k > len(food_times):
		ct = sum(i > loop for i in food_times)





food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))