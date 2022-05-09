def put_pos(keyboard, target):
	for x in range(2):
		for y in range(10):
			if keyboard[x][y] == target:
				return [x, y]

def put_dis(keyboard, pos, target):
	# t_pos = []
	for x in range(2):
		for y in range(10):
			if keyboard[x][y] == target:
				t_pos = [x, y]
				break
	men = abs(t_pos[0] - pos[0]) + abs(t_pos[1] - pos[1])
	var = abs(t_pos[1] - pos[1])
	return men, var

def solution(line):
	left = [1, 0]
	right = [1, 9]
	answer = []
	keyboard = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
				["Q","W","E","R", "T", "Y", "U", "I", "O", "P"]
				]
	for word in line:
		l_men, l_var = put_dis(keyboard, left, word)
		r_men, r_var = put_dis(keyboard, right, word)
		if l_men == r_men:
			if l_var == r_var:
				if word in ['1', '2', '3', '4', '5', 'Q', 'W', 'E', 'R', 'T']:
					answer.append(0)
					left = put_pos(keyboard, word)
				else:
					answer.append(1)
					right = put_pos(keyboard, word)
			else:
				if l_var < r_var:
					answer.append(0)
					left = put_pos(keyboard, word)
				else:
					answer.append(1)
					right = put_pos(keyboard, word)
		else:
			if l_men < r_men:
				answer.append(0)
				left = put_pos(keyboard, word)
			else:
				answer.append(1)
				right = put_pos(keyboard, word)
	return answer

solution("Q4OYPI")