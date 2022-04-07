# 럭키 스트레이트
# https://www.acmicpc.net/problem/18406

def solution():
    n = input()
    mid = len(n) // 2

    frnt = n[:mid] # 앞 숫자
    back = n[mid:] # 뒷 숫자

    if sum([int(i) for i in frnt]) == sum([int(i) for i in back]):
        print("LUCKY")
    else:
        print("READY")

solution()