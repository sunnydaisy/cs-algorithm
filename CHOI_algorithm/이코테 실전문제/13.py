# 치킨 배달
# https://www.acmicpc.net/problem/15686


#------------------------------------ 해설
# from itertools import combinations

# def get_num(candidate, house, chicken):
# 	result = 0
# 	for hx, hy in house:
# 		temp = 1e9
# 		for cx, cy in chicken:
# 			temp = min(temp, abs(hx - cx) + abs(hy - cy))
# 		result += temp
# 	return result

# def solution():
# 	n, m = map(int, input().split())
# 	chicken, house = [], []
	
# 	for i in range(n):
# 		line  = list(map(int, input().split()))
# 		for j in range(len(line)):
# 			if line[j] == 1: 				# 집인 경우 
# 				house.append((i, j))
# 			elif line[j] == 2:				# 치킨집인경우
# 				chicken.append((i, j))
	
# 	candidates = list(combinations(chicken, m))
# 	result = 1e9
# 	for candidate in candidates:
# 		result = min(result, get_num(candidate, house, chicken))
# 	return result



#---------------- 시도 1 : 정답 (굳이 length 함수를 만들지 않고 abs 함수를 사용하면 절대값을 구할 수 있었다. )
# import itertools

# def length(a, b):
# 	result = 0
# 	if a[0] > b[0]:
# 		result += a[0] - b[0]
# 	else:
# 		result += b[0] - a[0]
# 	if a[1] > b[1]:
# 		result += a[1] - b[1]
# 	else:
# 		result += b[1] - a[1]
# 	return result
	

# def solution():
# 	n, m = map(int, input().split())
# 	store = []
# 	house = []
# 	len_house = []
# 	for i in range(n):
# 		line  = list(map(int, input().split()))
# 		for j in range(len(line)):
# 			if line[j] == 1: 				# 집인 경우 
# 				house.append([i, j])
# 			elif line[j] == 2:				# 치킨집인경우
# 				store.append([i, j])
# 	for h in house:
# 		tmp = []
# 		for s in store:
# 			tmp.append(length(h, s))
# 		len_house.append(tmp.copy())
# 	com_list = list(itertools.combinations([i for i in range(len(len_house[0]))], m))
# 	result = int(1e9)
# 	for c_list in com_list:
# 		total_sum = 0
# 		for ho in len_house:
# 			min_tmp = int(1e9)
# 			for i in c_list:
# 				min_tmp = min(min_tmp, ho[i])
# 			total_sum += min_tmp
# 		result = min(result, total_sum)
# 	return result

print(solution())