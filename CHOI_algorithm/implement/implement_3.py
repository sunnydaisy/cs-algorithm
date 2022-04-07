# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

# 1회차
def solution(s):
    
    return 




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

# def tr2solution(s):
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


s = "aabaabaabaaaaaaab"
print(solution(s))

