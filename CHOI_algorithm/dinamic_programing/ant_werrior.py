# n = int(input())
# storages = list(map(int, input().split()))

n = 7
storages = [1, 3, 1, 5, 7, 7, 8]

# 해설
d = [0] * 100

d[0] = storages[0]
d[1] = max(storages[0], storages[1])
for i in range(2, n):
	d[i] = max(d[i - 1], d[i - 2] + storages[i])

print(d[n - 3])



# 시도 2

# d = [[0]] * 1001
# d[1] = [storages[0]]
# d[2] = [0, storages[1]]
# d[3] = [storages[0],storages[2]]
# # x 가 0 이 아니였을 떄 앞에 값들에 합
# def memo(x):

# 	if sum(d[x]) != 0:
# 		return d[x]

# 	tmp_1 = memo(x - 1) + [0]
# 	tmp_2 = memo(x - 2) + [storages[x - 1]]
# 	if sum(tmp_1) > sum(tmp_2):
# 		d[x] = tmp_1
# 	else:
# 		d[x] = tmp_2
# 	return d[x]
# memo(n)
# print(sum(d[n]))




# 시도 1
# tmp = [0] + storages.copy()
# ans = [0] * 1001

# ans[1] = tmp[1]

# def recur(x):
# 	if ans[x] != 0:
# 		return ans[x]
# 	if recur(x + 1) + recur(x - 1) > tmp[x]:
# 		tmp[x] = 0
# 	ans[x] = tmp[x]
# 	return tmp[x]

# recur(n)
# print(sum(tmp))







