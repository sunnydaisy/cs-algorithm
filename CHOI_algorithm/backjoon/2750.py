# 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys

#---------------- 실패 : 음수도 포함이다
# def solution(): 
#     n = int(sys.stdin.readline())
#     array = [0] * 1001
#     for _ in range(n):
#         array[int(sys.stdin.readline())] = 1
#     for i in range(1, 1001):
#         if array[i] == 1:
#             print(i)

#---------------- 통과 68ms
def solution():
    n = int(sys.stdin.readline())
    array = []
    for _ in range(n):
        array.append(int(sys.stdin.readline()))
    array.sort()

    for i in array:
        print(i)

# --------------- 통과 108ms
# def solution():
#     n = int(input())
#     arr = []
#     for _ in range(n):
#         arr.append(int(input()))
#     arr.sort()
#     for i in arr:
#         print(i)


# --------------- int로 안바꿔서 실패
# def solution():
#     n = int(sys.stdin.readline().rstrip())
#     array = []
#     for _ in range(n):
#         array.append(sys.stdin.readline().rstrip())
#     array.sort()

#     for i in array:
#         print(i)

solution()