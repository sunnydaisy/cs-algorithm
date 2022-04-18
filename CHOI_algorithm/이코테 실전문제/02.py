# 곱하기 혹은 더하기

# 2회차
def tr1():
	str_num = input()
	result = 1
	for i in str_num:
		if i == '0':
			continue
		if i == '1':
			result += 1
		else:
			result *= int(i)
	print(result)

tr1()
# 이번에도 1회차와 마찬가지로 1이 들어올 때의 경우의 수를 간과했다.












# 1회차

# num_list = [int(i) for i in list(input())]
# result = 0

# for i in num_list:
# 	if i <= 1 or result <= 1:
# 		result += i
# 	else:
# 		result *= i
# print(result)
# 1이 오는 경우에 더하는 것 더 높은 결과라는 것을 놓쳤다


"""
testcase

02984
answer : 576

567
answer : 210

02145
asnwer : 60

"""