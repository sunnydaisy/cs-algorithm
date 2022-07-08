count = 0

def solution(numbers, target):
	global count
	visited = [False] * len(numbers)

	if (sum(numbers) == target):
		return 1

	for i in range(len(numbers)):
		dfs(numbers, i, visited, target)

	return count


def dfs(numbers, i, visited, target):
	visited[i] = True
	print(visited, sumCk(numbers, visited), target)
	
	if sumCk(numbers, visited) == target:
		global count
		count += 1
	for j in range(i+1, len(numbers)):
		dfs(numbers, j, visited, target)
	visited[i] = False


def sumCk(numbers, visited):
	tmp = 0
	for i in range(len(numbers)):
		if visited[i]:
			tmp -= numbers[i]
		else:
			tmp += numbers[i]
	return tmp

print(solution([1,1,1,1,1], 3))

# --------------------------------- 2회차 실패 dfs 를 못만들고있음
# def solution(numbers, target):
# 	answer = 0
# 	visited = [False] * len(numbers)

# 	if (sum(numbers) == target):
# 		return 1

# 	for i in range(len(numbers)):
# 		visited[i] = True
# 		answer += dfs(numbers, i, target, visited)
# 		visited[i] = False

# 	return answer

# def dfs(numbers, idx, target, visited):
# 	print(visited, idx)
	
# 	if idx == len(numbers) and sumCk(numbers, visited) == target:
# 		return 1
	
	
# 	if idx == 0:
# 		print("!!!!!!")
# 	count = 0
	
# 	for i in range(idx + 1, len(numbers)):
# 		visited[i] = True
# 		count += dfs(numbers, i, target, visited)
# 		visited[i] = False
# 	if idx == 0:
# 		print("FFFFFFFF")
	
# 	return count

# def sumCk(numbers, visited):
# 	tmp = 0
# 	for i in range(len(numbers)):
# 		if visited[i]:
# 			tmp -= numbers[i]
# 		else:
# 			tmp += numbers[i]
# 	return tmp

# print(solution([1,1,1,1,1], 2))




# ------------------------------------- 1회차 실패

# def solution(numbers, target):
#     if (sum(numbers) < target):
#         return 0
#     elif (sum(numbers) == target):
#         return 1
#     elif (-sum(numbers) == target):
#         return 1
#     answer = 0
	
	
#     for i in range(len(numbers)):
#         visited = [False] * len(numbers)
#         answer += dfs(numbers, i, visited, target)
#     return answer


# def dfs(numbers, i, visited, target):
	
#     count = 0
#     if (i >= len(numbers)):
#         return 0
#     if (visited[i]):
#         return 0
#     print(target, visited)
#     visited[i] = True
#     sumNum = 0
#     for q in range(len(numbers)):
#         if visited[q]:
#             sumNum -= numbers[q]
#         else:
#             sumNum += numbers[q]
#     # print(target, visited)
#     if (sumNum == target):
#         # print(target, visited)
#         return 1
	

#     for j in range(i+1, len(visited)):
#         count += dfs(numbers, j, visited, target)
#     visited[i] = False
#     return count