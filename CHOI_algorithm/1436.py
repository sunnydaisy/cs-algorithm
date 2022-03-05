# 영화감독 숌
# https://www.acmicpc.net/problem/1436

def print_666(front, back):
	print(front, end='') if front != 0 else None
	print('666' + str(back)) if back != 0 else print('666')


def solution():
	n = int(input())
	front = -1
	back = 0
	for _ in range(n + 1):
		if front % 10 == 6:
			back += 1
			if back % 10 == 9:
				front += 1
		else:
			back = 0
			front += 1
	print_666(front, back)
			
solution()
