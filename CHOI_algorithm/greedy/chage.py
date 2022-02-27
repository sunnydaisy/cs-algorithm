# 거스름돈 문제

from time import time

def solution():
	N = int(input())
	result = 0

	result += N // 500 
	N = N % 500
	result += N // 100 
	N = N % 100
	result += N // 50 
	N = N % 50
	result += N // 10 
	N = N % 10
	
	print(result)


def answer():
	N = int(input())
	result = 0	
	coin_type = [500, 100, 50, 10]
	for i in coin_type:
		result += N // i
		N %= i
	print(result)


now = time()
solution()
# answer()
end = time()
print(f"time : {end - now}")