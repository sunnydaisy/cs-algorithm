# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

# 1회차

# -----------4번째------------- 100점 : 문제를 다시 이해한 뒤에 다른 방법으로 풀어보니까 풀림
def div_ck(s, scale):
	i = 0
	div_arr = []
	result = 0
	while i < len(s):
		div_arr.append(s[i:i+scale])
		i += scale
	tmp = None
	cnt = 1
	for i in div_arr:
		if tmp is None: # 반복문이 처음 일 때
			tmp = i
			result += len(tmp)
			continue
		if i == tmp:  # 이전 단어와 같을 떄
			cnt += 1
		else:
			if cnt != 1:
				result += len(str(cnt))
				cnt = 1
			tmp = i
			result += len(i)
	if cnt > 1:
		result += len(str(cnt))
	return result


def solution(s):
	scale = len(s) // 2
	result = len(s)

	while scale >= 1:
		result = min(result, div_ck(s, scale))
		scale -= 1
	return result


# -----------3번쨰------------- 60 점 : 지금까지 문제를 잘못했는데 이번에는 왜 틀렸는지 모르겠음
# def div_ck(s, scale):
# 	i = 0
# 	result = 0
# 	cnt = 1
# 	while i < len(s):
# 		frnt = s[i:scale + i] # 앞 부분
# 		back = s[scale + i :] # 뒷 부분
# 		if len(frnt) > len(back):
# 			if cnt == 1: # 같은게 없었는데 끝난경우
# 				result += len(s[i:])
# 			else:
# 				result += len(str(cnt)) + len(frnt) + len(back)
# 			break
# 		if frnt == back[:len(frnt)]: # 일치하는 경우
# 			cnt += 1
# 			i += len(frnt) # i 
# 		else:
# 			if cnt > 1:
# 				result += len(str(cnt)) + len(frnt)
# 				i += len(frnt) # 이미 같은 적이 있어서 그 길이만큼은 지나가야함
# 				cnt = 1
# 			else:
# 				if i == 0: # 처음부터 잘려야한다
# 					result += len(frnt)
# 					i += len(frnt)
# 				else:
# 					result += 1
# 					i += 1
# 	return result

# def solution(s):
# 	scale = len(s) // 2
# 	result = len(s)
# 	tmp = 0
# 	while scale >= 1:
# 		result = min(result, div_ck(s, scale))
# 		scale -= 1
# 	return result





# def div_ck(s, scale): # 크기를 정하고 먼저 큰 크기부터 나누는 방식으로 하려고 했으나 이렇게되면 aabaabb의 경우 2aa2bb 이런식으로 될거같다
# 	idx = 0
# 	cnt = 1 # 중복되는 단어 개수
# 	result = ""
# 	tmp = ""
# 	while idx < len(s):
# 		frnt = s[idx:scale + idx] # 앞 부분
# 		back = s[scale + idx :] # 뒷 부분
# 		if len(frnt) > len(back):
# 			return cnt
# 		if frnt == back[:len(frnt)]: # 일치하는 경우
# 			cnt += 1
# 			idx += len(frnt) # idx 
# 		else:  # 일치하지 않는 경우
# 			if cnt > 1:
# 				result += str(cnt) + frnt
# 				cnt = 1
# 			else:
# 				if len(tmp)
# 				tmp += s[idx]
# 			idx += 1
# 	return result

# def solution(s):
# 	div_scale = len(s) // 2 # 나누는 단위
# 	# div_ck(s, div_scale, 0)
# 	return div_ck(s, 3)


# def div_ck(s, scale):
#     idx = 0
#     cnt = 1 # 중복되는 단어 개수
#     while idx < len(s):
#         frnt = s[idx:scale + idx] # 앞 부분
#         back = s[scale + idx :] # 뒷 부분
#         if len(frnt) > len(back):
#             return cnt
#         if frnt == back[:len(frnt)]: # 일치하는 경우
#             cnt += 1
#             idx += len(frnt) # idx 
#         else:  # 일치하지 않는 경우
#             if cnt > 1:
#                 return cnt
#             idx += 1
# def tr_1solution(s):
#     div_scale = len(s) // 2 # 나누는 단위
#     # div_ck(s, div_scale, 0)
#     return div_ck(s, 3)


s = "abcabcabcabcdededededede"
print(solution(s))

