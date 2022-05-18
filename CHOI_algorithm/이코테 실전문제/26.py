# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

# ----------------------------------- 2회차 : 성공 208ms : 힙규로 해결
import sys
import heapq

def solution():
	n = int(input())
	q = []
	
	for _ in range(n):
		heapq.heappush(q, int(sys.stdin.readline()))

	min_tmp = min(q)
	tmp = 0
	result = 0
	while q:
		a = heapq.heappop(q)
		if len(q) == 0:
			# result += a
			break
		b = heapq.heappop(q)
		result += a + b
		heapq.heappush(q, a + b)
		

		
	
	print(result)

solution()


# --------------------------------------------1 회차 : 실패 : 그냥 정렬해서 앞에서 부터 더했는데 예외 케이스가 있음 30 40 50 60
# def solution():
# 	n = int(input())
# 	arr = []
# 	for _ in range(n):
# 		arr.append(int(sys.stdin.readline()))
# 	arr.sort()
# 	tmp = 0
# 	result = 0
# 	for i in arr:
# 		tmp += i
# 		result += tmp
# 	result -= arr[0]
# 	print(result)

# solution()

"""
30 40 50 60
70 + 110 + 180
70
110



"""