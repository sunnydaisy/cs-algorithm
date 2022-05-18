# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060



from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, rigth_value):
	rigth_index = bisect_right(a, rigth_value)
	left_index = bisect_left(a, left_value)
	return rigth_index - left_index

def solution(words, queries):
	result = []
	n = len(words)
	array = [[] for _ in range(10001)]
	reverse_array = [[] for _ in range(10001)]

	for word in words:
		array[len(word)].append(word)
		reverse_array[len(word)].append(word[::-1])
	
	for i in range(1, 10001):
		array[i].sort()
		reverse_array[i].sort()

	for que in queries:
		if que[0] != "?":
			res = count_by_range(array[len(que)], que.replace('?', 'a'), que.replace('?', 'z'))
		else:
			res = count_by_range(reverse_array[len(que)], que[::-1].replace('?', 'a'), que[::-1].replace('?','z'))
		result.append(res)
	return result




# ------------------------------------ 시도 3 : 실패
# def strcmp(a, b):
# 	i = 0
# 	min_len = min(len(a), len(b))
# 	while i < min_len and a[i] == b[i]:
# 		i += 1
# 	if i == min_len:
# 		return 1
# 	if a[i] != b[i]:
# 		return ord(a[i])


# def left_idx(array, target):
# 	start = 0
# 	end = len(array) - 1
# 	while start <= end:
# 		mid = (start + end) // 2
# 		if array[mid] == target:
# 			start = mid + 1
# 			pivot = max(pivot, mid)
# 		else:
# 			end = mid - 1
# 	return (0, array[pivot + 1:], pivot)


# def count_index(string, target):
# 	start = 0
# 	end= len(string) - 1
	
# 	if string[0] == target: # ??****  앞에 ?
# 		pivot = 0
# 		while start <= end:
# 			mid = (start + end) // 2
# 			if string[mid] == target:
# 				start = mid + 1
# 				pivot = max(pivot, mid)
# 			else:
# 				end = mid - 1
# 		return (0, string[pivot + 1:], pivot)
# 	else: # ***???				뒤에 ?
# 		pivot = 1e9
# 		while start <= end:
# 			mid = (start + end) // 2
# 			if string[mid] == target:
# 				end = mid - 1
# 				pivot = min(pivot, mid)
# 			else:
# 				start = mid + 1
# 		return (1, string[:pivot], pivot)


# def solution(words, queries):
# 	answer = []
# 	for que in queries:
# 		count = 0
# 		f_b, str, pivot = count_index(que, "?")
# 		str_len = len(str)
# 		if f_b == 0:	# ???***
# 			for word in words:
# 				# print(word[pivot + 1:])
# 				if len(word) == len(que) and word[pivot + 1:] == str:
# 					count += 1
# 		else:			# **????
# 			for word in words:
# 				# print(word[:pivot])
# 				if len(word) == len(que) and word[:pivot] == str:
# 					count += 1
# 		answer.append(count)

	
# 	return answer






# def strcmp(a, b):
# 	i = 0;
# 	while i < len(b):
# 		if a[i] != b[i]:
# 			return ord(a[i]) - ord(b[i])
# 		i += 1
# 	if len(a) == len(b):
# 		return 0
# 	else:
# 		return 1

# # def count_word(arr, target):
# # 	start = 0
# # 	end = len(arr) - 1
# # 	while start <= end:
# # 		mid = (start + end) // 2
# # 		if strcmp(arr[mid], target)

# def left_inx(arr, target):
# 	start = 0
# 	end = len(arr) - 1
# 	result = 0
# 	while start <= end:
# 		mid = (start + end) // 2
# 		if strcmp(arr[mid], target) >= 0 : # 같거나 오른쪽에 있는 경우
# 			end = mid - 1
# 			result = max(result, mid)
# 		else:
# 			start = mid + 1
# 	return result

# def right_inx(arr, target):
# 	start = 0
# 	end = len(arr) - 1
# 	result = end
# 	while start <= end:
# 		mid = (start + end) // 2
# 		if strcmp(arr[mid], target) <= 0 : # 
# 			end = mid - 1
# 			result = min(result, mid)
# 		else:
# 			start = mid + 1
# 	return result - 1



# def count_index(string, target):
# 	start = 0
# 	end= len(string) - 1
	
# 	if string[0] == target: # ??****  앞에 ?
# 		pivot = 0
# 		while start <= end:
# 			mid = (start + end) // 2
# 			if string[mid] == target:
# 				start = mid + 1
# 				pivot = max(pivot, mid)
# 			else:
# 				end = mid - 1
# 		return (0, string[pivot + 1:], pivot)
# 	else: # ***???				뒤에 ?
# 		pivot = 1e9
# 		while start <= end:
# 			mid = (start + end) // 2
# 			if string[mid] == target:
# 				end = mid - 1
# 				pivot = min(pivot, mid)
# 			else:
# 				start = mid + 1
# 		return (1, string[:pivot], pivot)


# def solution(words, queries):
# 	answer = []
# 	words.sort()
# 	for que in queries:
# 		count = 0
# 		f_b, str, pivot = count_index(que, "?")
# 		str_len = len(str)
# 		if f_b == 0:	# ???***
# 			answer.append(right_inx(words, str) - left_inx(words, str) + 1)
# 			# for word in words:
# 			# 	# print(word[pivot + 1:])
# 			# 	if len(word) == len(que) and word[pivot + 1:] == str:
# 			# 		count += 1
# 		else:			# **????
# 			answer.append(right_inx(words, str) - left_inx(words, str) + 1)
# 			# for word in words:
# 			# 	# print(word[:pivot])
# 			# 	if len(word) == len(que) and word[:pivot] == str:
# 			# 		count += 1
# 		answer.append(count)

	
# 	return answer






# -------------------------- 1회차 : 효율성 2불
# def count_index(string, target):
# 	start = 0
# 	end= len(string) - 1
	
# 	if string[0] == target: # ??****  앞에 ?
# 		pivot = 0
# 		while start <= end:
# 			mid = (start + end) // 2
# 			if string[mid] == target:
# 				start = mid + 1
# 				pivot = max(pivot, mid)
# 			else:
# 				end = mid - 1
# 		return (0, string[pivot + 1:], pivot)
# 	else: # ***???				뒤에 ?
# 		pivot = 1e9
# 		while start <= end:
# 			mid = (start + end) // 2
# 			if string[mid] == target:
# 				end = mid - 1
# 				pivot = min(pivot, mid)
# 			else:
# 				start = mid + 1
# 		return (1, string[:pivot], pivot)


# def solution(words, queries):
# 	answer = []
# 	for que in queries:
# 		count = 0
# 		f_b, str, pivot = count_index(que, "?")
# 		str_len = len(str)
# 		if f_b == 0:	# ???***
# 			for word in words:
# 				# print(word[pivot + 1:])
# 				if len(word) == len(que) and word[pivot + 1:] == str:
# 					count += 1
# 		else:			# **????
# 			for word in words:
# 				# print(word[:pivot])
# 				if len(word) == len(que) and word[:pivot] == str:
# 					count += 1
# 		answer.append(count)

	
# 	return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],	["fro??", "????o", "fr???", "fro???", "pro?"])