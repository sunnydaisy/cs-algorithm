# 큰 수의 법칙
from time import time
from unittest import result

# N, M, K = map(int, input().split())
# num_list = list(map(int, input().split()))
start = time()
N, M, K = 5, 8, 3
num_list = [2, 4, 5, 4, 6]

# 1 		time : 8.106231689453125e-06
# num_list.sort(reverse=True)
# result = 0
# count = 0
# while count != M:
# 	for _ in range(K):
# 		if count == M:
# 			break
# 		result += num_list[0]
# 		count += 1
# 	if count == M:
# 		break
# 	result += num_list[1]
# 	count += 1


# 2
num_list.sort(reverse=True)

result = 0

first = num_list[0]
second = num_list[1]

count = (M // (K + 1))
result = second * count + first * (count + M % (K + 1)) * K


end = time()


print(result)
print(f"time : {end - start}")