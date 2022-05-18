# 공유기 설치
# https://www.acmicpc.net/problem/2110

import sys

def solution():
    n, c = map(int, input().split())
    array = []
    for _ in range(n):
        array.append(int(sys.stdin.readline().rstrip()))

    array.sort()
    start = 1                   # 가능 최소 거리
    end = array[-1] - array[0]  # 가능 최대 거리
    result = 0
    while start <= end:

        mid = (end + start) // 2   # gap 을 의미
        target = array[0]   # 공유기 설치 위치   맨 처음부분에 설치를 무조건 적으로 해도 된다. 왜냐하면 뒤에 부터 설치 했을 떄 가능하는 경우면 첫번째도 가능해야하기 때문
        count = 1           # 공유기 설치 개수

        for i in range(1, n):
            if array[i] >= mid + target:
                target = array[i]
                count += 1
        if c > count: # 부족한 경우
            end = mid - 1
        else:
            start = mid + 1
            result = max(result, mid)
    print(result)
    return result

solution()
