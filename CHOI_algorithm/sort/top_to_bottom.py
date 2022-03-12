n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

tmp = [0] * (max(num_list) + 1)
for i in num_list:
    tmp[i] += 1

for i in range(len(tmp) - 1, 0, -1):
    for j in range(tmp[i]):
        print(i, end=' ')

