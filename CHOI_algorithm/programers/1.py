# 파일명 정렬

def solution(files):
	splited_list = []
	num = "0123456789"
	for file in files:
		tmp = []
		i = 0
		while i < len(file) and file[i] not in num:
			i += 1
		tmp.append(file[:i].upper())
		tmp.append(file[:i]) # add word 
		start_tmp = i
		if len(file) <= i:
			splited_list.append(tmp)
			continue
		while i < len(file) and file[i] in num:
			i += 1
		if len(file) <= i:
			splited_list.append(tmp)
			continue
		tmp.append(file[start_tmp:i]) # add num
		tmp.append(file[i:]) # add tail
		splited_list.append(tmp)
	
	splited_list.sort(key=lambda x : (x[0], int(x[2])) if len(x) >= 2 else x[0])
	answer = []
	for i in splited_list:
		tmp = ""
		n = 1
		while n < len(i):
			tmp += i[n]
			n += 1

		answer.append(tmp)
		
	return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
solution(files)