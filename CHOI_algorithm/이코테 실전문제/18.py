# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058


# -------------------------------------- 시도 1 : 정답

# def order_ck(arr): # 올바른 문자열인지 확인
# 	stack = []
# 	for i in arr:
# 		if i == '(':
# 			stack.append(i)
# 		else:
# 			if len(stack) == 0: # 비어 있는 경우
# 				return False
# 			stack.pop()
# 	if len(stack) != 0:
# 		return False
# 	return True

# def reverse(str):
# 	result = ''
# 	for i in str:
# 		if i == '(':
# 			result += ')'
# 		else:
# 			result += '('
# 	return result

# def solution(p):
# 	if p == '':
# 		return ''
# 	stack = []
# 	point = 0
# 	for i in range(len(p)):
# 		if len(stack) == 0:
# 			if i == 0:
# 				stack.append(p[i])
# 				continue
# 			point = i
# 			break
# 		else:
# 			tmp = stack.pop()
# 			if tmp != p[i]:
# 				continue
# 			else:
# 				stack.append(tmp)
# 				stack.append(p[i])
# 	if point == 0: # 둘로 안나눠지고 끝났을 떄
# 		u = p
# 		v = ''
# 	else:
# 		u = p[:point]
# 		v = p[point:]

# 	if order_ck(u):
# 		return u + solution(v)
# 	else:
# 		return '(' + solution(v) + ')' + reverse(u[1:-1])



# p = ")("
# print(solution(p))