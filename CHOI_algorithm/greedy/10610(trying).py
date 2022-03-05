# n = str(input())

n = '201'

def make_num(list):
	result = 0
	for i in list:
		result = result * 10 + i
	return (result)

def solution(n):
	result = 0
	if '0' not in n:
		print(-1)
		return
	num_list = [int(x) for x in n]
	num_list.sort(reverse=True)

	
	result = make_num(num_list)
	if result % 30 == 0:
		return (result)
	
