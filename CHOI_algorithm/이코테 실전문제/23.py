# 국영수
# https://www.acmicpc.net/problem/10825

# ----------------- 람다로 튜플을 정리하는 방법
import sys

def solution():
	n = int(input())
	all = []
	for _ in range(n):
		all.append(list(sys.stdin.readline().split()))
	all.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
	for i in all:
		print(i[0])

solution()