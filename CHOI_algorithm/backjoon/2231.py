def maker(nb):
	ret = nb
	while nb > 0:
		ret += nb % 10
		nb = int(nb / 10)
	return ret

def solution(nb):
	flag = 0
	min = nb
	ck = int(nb / 2)
	while ck < nb:
		if maker(ck) == nb and min > ck:
			flag = 1
			min = ck
		ck += 1
	if flag == 0:
		return 0
	return min

n = int(input())
solution(n)
