# 연산자 끼워 넣기
# https://www.acmicpc.net/problem/14888


# ---------------------------------- 중복조합시도 : 정답 568ms
# import sys
# from itertools import permutations

# def solution():
# 	INF = int(1e9)
# 	max_num = -INF
# 	min_num = INF

# 	n = int(input())
# 	num_arr = list(map(int, sys.stdin.readline().split())) 
# 	op_arr = list(map(int, sys.stdin.readline().split()))
# 	op_str = []
# 	for idx, value in enumerate(op_arr):
# 		op_str += [idx] * value
# 	op_str = set(permutations(op_str, n - 1))
# 	for ops in op_str:
# 		tmp = num_arr[0]
# 		for num, op in zip(num_arr[1:], ops):
# 			if op == 0:
# 				tmp += num
# 			elif op == 1:
# 				tmp -= num
# 			elif op == 2:
# 				tmp *= num
# 			else:
# 				tmp = int(tmp / num)
# 		max_num = max(max_num, tmp)
# 		min_num = min(min_num, tmp)
# 	print(max_num)
# 	print(min_num)
		
# solution()





# --------------- 해설 : 116ms 그냥 무식하게 돌리면 되는걸 생각 못함 
# import sys

# INF = int(1e9)
# max_num = -INF
# min_num = INF

# n = int(input())
# num_arr = list(map(int, sys.stdin.readline().split())) 
# add, sub, mul, div = list(map(int, sys.stdin.readline().split()))

# def dfs(i, now):

# 	global max_num, min_num, n, add, sub, mul, div
# 	if i == n:
# 		max_num = max(max_num, now)
# 		min_num = min(min_num, now)
# 	else:
# 		if add > 0:
# 			add -= 1
# 			dfs(i + 1, now + num_arr[i])
# 			add += 1
# 		if sub > 0:
# 			sub -= 1
# 			dfs(i + 1, now - num_arr[i])
# 			sub += 1
# 		if mul > 0:
# 			mul -= 1
# 			dfs(i + 1, now * num_arr[i])
# 			mul += 1
# 		if div > 0:
# 			div -= 1
# 			dfs(i + 1, int(now / num_arr[i]))
# 			div += 1
		

# dfs(1, num_arr[0])
# print(max_num)
# print(min_num)


# ------------------------------ 1회차 : 실패 (항상 합보다 곱이 먼저오면 최대값이 된다고 생각했는데 합이 먼저 오고 곱이 오는게 최대값이 될 수 있다는 생각에 포기)

# def max_num(num_arr, op_arr):
# 	plus = 0
# 	multi = 0
# 	for i in op_arr:
# 		if i

# def solution():
# 	n = int(input())
# 	num_arr = list(map(int, sys.stdin.readline().split())) 
# 	op_arr = list(map(int, sys.stdin.readline().split()))

# 	plus = 0
# 	minus = 0
# 	muti = 0
# 	div = 0
# 	for i in op_arr:
# 		if i == 0:
# 			plus += 1
# 		elif i == 1:
# 			minus += 1
# 		elif i == 2:
# 			muti += 1
# 		elif i == 3:
# 			div += 1

# 	tmp_plus = plus
# 	tmp_minus = minus
# 	tmp_muti = muti
# 	tmp_div = div

# 	max_num = None
# 	for i in num_arr:
# 		if max_num == None:
# 			max_num = i
# 		elif max_num > 0:	# 양수인 경우
# 			pass
# 		else:				# 음수인 경우



