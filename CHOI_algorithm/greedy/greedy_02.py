# 곱하기 혹은 더하기

num_list = [int(i) for i in list(input())]
result = 0

for i in num_list:
	if i <= 1 or result <= 1:
		result += i
	else:
		result *= i
print(result)
# 1이 오는 경우에 더하는 것 더 높은 결과라는 것을 놓쳤다