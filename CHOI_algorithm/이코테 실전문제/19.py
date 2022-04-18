# 연산자 끼워 넣기
# https://www.acmicpc.net/problem/14888

import sys

def max_num(num_arr, op_arr):
	plus, minus, muti, div = op_arr


def solution():
	n = int(input())
	num_arr = list(map(int, sys.stdin.readline().split())) 
	op_arr = list(map(int, sys.stdin.readline().split()))

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




solution()