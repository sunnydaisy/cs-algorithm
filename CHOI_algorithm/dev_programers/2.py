def split(room):
	for i in range(len(room)):
		if room[i] == "]":
			return [int(room[1:i])] + room[i+1:].split(",")

def solution(rooms, target):
	dic = {}
	# dic["hs"] = 2
	new_list = []
	for room in rooms:
		splited = split(room)
		for i in splited[1:]:
			if i in dic:
				dic[i].append(splited[0])
			else:
				dic[i]=[splited[0]]
	rank = []
	for name in dic:
		if target in dic[name]:
			continue
		min_diff = 1e9
		for num in dic[name]:
			min_diff = min(min_diff, abs(target - num))
		tmp = [name, min_diff, len(dic[name])]
		rank.append(tmp)
	rank.sort(key=lambda x : (x[2], x[1], x[0]))
	result = []
	for i in rank:
		result.append(i[0])
	return result
	# 	new_list.append(splited)
		

	# rank = []
	# name_list = []
	# for room in new_list:
	# 	if room[0] == target:
	# 		pass
	# 	else:
	# 		for name in room[1:]:
				# rank.append([abs(target - room[0]), name])

solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"], 403)