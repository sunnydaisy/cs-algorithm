# 체스판 칠하기
# https://www.acmicpc.net/problem/1018
import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
	line = list(map(str, sys.stdin.readline().split()))
	print(line[0])

print(board)