# 문자열 뒤집기
# https://www.acmicpc.net/problem/1439

# 2회차
def tr1():
	str_num = input()
	status = False
	now = None
	result = 0
	for i in str_num:
		if now != i:
			now = i
			if status == False:
				status = True
			else:
				status = False
				result += 1
	print(result)

tr1()
# 답보다 내가 하는 방법이 더 좋은듯













# 1회차
# s = input()

# tmp = []
# count = 0
# flag = 0

# for i in range(len(s)):
# 	if i == 0 or int(s[i]) != tmp[-1]:
# 		tmp.append(int(s[i]))

# for i in range(len(tmp)):
# 	if i == 0:
# 		flag = tmp[0]
# 	elif flag != tmp[i]:
# 		count += 1

# print(count)
# 단순하게 앞에 숫자랑 다를때를 확인하면 되는데 더 복잡하게 푼듯


"""
1111111 
answer : 0

101 
answer : 1

10001 
answer : 1

1001000 
answer : 2

1001001 
answer : 2

1001010001 
answer : 4

100100100 
answer : 3

"""