# https://www.acmicpc.net/problem/2750
import sys

def solution():
    n = int(sys.stdin.readline().rstrip())
    array = []
    for _ in range(n):
        array.append(sys.stdin.readline().rstrip())
    array.sort()

    for i in array:
        print(i)

solution()