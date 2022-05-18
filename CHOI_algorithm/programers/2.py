# 전화번호 접두사 중복 

def solution(phone_book):
	phone_book.sort()
	for i in range(len(phone_book)):
		for j in range(i, len(phone_book)):
			if i == j:
				continue
			if phone_book[i][0] != phone_book[j][0]:
				continue
			i_len = len(phone_book[i])
			j_len = len(phone_book[j])
			if i_len < j_len:
				if phone_book[i] == phone_book[j][:i_len]:
					return False
			else:
				if phone_book[j] == phone_book[i][:j_len]:
					return False
	return True

solution(	["119", "97674223", "1195524421"])