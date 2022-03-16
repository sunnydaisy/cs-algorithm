# 계수 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

tmp = [0] * (max(array) + 1)

for i in array:
    tmp[i] += 1

for i in range(len(tmp)):
    for j in range(tmp[i]):
        print(i, end=' ')