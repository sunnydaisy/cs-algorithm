n, m = map(int, input().split())
n_list = list(map(int, input().split()))


diff = lambda a, b : a - b if a > b else b - a


def solution(n_list):
	n_list.sort()
	i = 0
	ret = n_list[0] + n_list[1] + n_list[2]
	#print(n_list)
	for j in n_list:
		for q in n_list[i + 1: n - 1]:
			for r in n_list[i + 2:]:
				tmp = j + q + r
				#print(j, q, r)
				if m - tmp >= 0 and diff(tmp, m) < diff(ret, m):
					ret = tmp
					if ret == m:
						return ret
		#print("#")
		i += 1
	return ret



print(solution(n_list))

