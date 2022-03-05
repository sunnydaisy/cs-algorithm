# 문자열 뒤집기
s = input()

tmp = []
count = 0
flag = 0

for i in range(len(s)):
	if i == 0 or int(s[i]) != tmp[-1]:
		tmp.append(int(s[i]))

for i in range(len(tmp)):
	if i == 0:
		flag = tmp[0]
	elif flag != tmp[i]:
		count += 1

print(count)
# 단순하게 앞에 숫자랑 다를때를 확인하면 되는데 더 복잡하게 푼듯