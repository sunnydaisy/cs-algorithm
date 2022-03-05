# 체스판 칠하기
# https://www.acmicpc.net/problem/1018

import sys

def solution():
	n, m = map(int, sys.stdin.readline().split())
	if n < 8 or m < 8:
		print(0)
	board = []
	for _ in range(n):
		line = list(map(str, sys.stdin.readline().split()))
		print(line[0])

	print(board)