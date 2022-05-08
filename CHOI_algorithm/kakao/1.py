from re import S
from secrets import choice


def solution(survey, choices):
	score = {"R" : 0, "T" : 0, 
			"F" : 0, "C" : 0, 
			"M" : 0, "J" : 0, 
			"A" : 0, "N" : 0, }

	n = len(survey)
	for i in range(n):
		answer = survey[i]
		# if answer == "RT" or answer == "TR":
		s = choices[i] # 동의 비동의 점수
		if s < 4 : # 비동의 경우
			score[answer[0]] += 4 - s
		elif s > 4: # 동의인 경우
			score[answer[1]] += s - 4
	answer = ''
	if score["R"] >= score["T"]:
		answer += "R"
	elif score["R"] < score["T"]:
		answer += "T"

	if score["F"] > score["C"]:
		answer += "F"
	elif score["F"] <= score["C"]:
		answer += "C"

	if score["J"] >= score["M"]:
		answer += "J"
	elif score["J"] < score["M"]:
		answer += "M"

	if score["A"] >= score["N"]:
		answer += "A"
	elif score["A"] < score["N"]:
		answer += "N"
	
	return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choice = [5, 3, 2, 7, 5]
solution(survey, choice)