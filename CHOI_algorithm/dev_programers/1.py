def solution(atmos):
	answer = 0
	left = -1
	for dust, cdust in atmos:
		if dust >= 81 or cdust >= 36:
			if left < 0:
				answer += 1
				if dust >= 151 and cdust >= 76:
					left = 0
				else:
					left = 2
			else:
				if dust >= 151 and cdust >= 76:
					left = 0
			left -= 1
		else:
			left -= 1
	return answer

print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))