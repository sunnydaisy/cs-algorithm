# 병사 배치하기
# https://www.acmicpc.net/problem/18353


# ----------------------------------------- 해설 소스코드 LIS 사용
# def solution():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.reverse()
#     dp = [1] * n
#     for i in range(1, n):
#         for j in range(0, i):
#             if arr[j] < arr[i]:
#                 dp[i] = max(dp[i], dp[j] + 1) 
#     print(n - max(dp)) # 1 1 2 3 2 4 5
    
# solution()





import random

def cnt(arr, f_idx, b_idx):
    ## <- 방향으로 바뀜
    f_tmp = arr[b_idx]
    b_count = 0
    for i in range(f_idx, -1, -1):
        if arr[i] < f_tmp:
            b_count += 1
        else:
            break
    ## -> 방향으로 바뀜
    b_tmp = arr[f_idx]
    f_count = 0
    for i in range(b_idx, len(arr)):
        if arr[i] > b_tmp:
            f_count += 1
        else:
            break

    result = min(b_count, f_count)
    if f_count < b_count: ## -> 방향으로 바꾸는게 맞으면
        arr = arr[:f_idx + 1] + arr[b_idx + f_count:]
    else:
        arr = arr[:f_idx - b_count + 1] + arr[b_idx:]
    return arr, result

def my_solution(n, arr):
    # n = int(input())
    # arr = list(map(int, input().split()))

    result = 0
    if len(arr) == 1:
        print(0)
        return 0
    
    i = 0
    while i < n:
        if i == 0:
            i += 1
            continue
        if arr[i - 1] > arr[i]:
            i += 1
            continue
        else: # 내림차순이 아닌 경우
            arr, ct = cnt(arr, i - 1, i)
            result += ct
            i = -1
            n = len(arr)
        i += 1
    # print(result)
    return result
my_solution(5, [10, 23, 19, 79, 96])
# solution()

# n = 5
# for _ in range(5):
#     arr = []
#     for _ in range(n):
#         arr.append(random.randrange(1, 100))
#     tmp = arr.copy()
#     tmp1 = arr.copy()
#     answer = solution(n, tmp)
#     my = my_solution(n, tmp1)
#     if answer != my:
#         print(arr)
#         print("answer   : ", answer)
#         print("my       : ", my)



"""

5
65 31 19 47 84
result : 2


5
10 23 19 79 96
result : 3


5
99 19 17 79 24 2
result : 2


5
64 24 79 24 2
result : 2




"""








# --------------------------- 값을 바꿔주는 방법으로 했지만 예외가 생김
# def cnt(arr, f_idx, b_idx):
#     ## <- 방향으로 바뀜
#     f_tmp = arr[b_idx]
#     b_count = 0
#     for i in range(f_idx, -1, -1):
#         if arr[i] < f_tmp:
#             b_count += 1
#         else:
#             break
#     ## -> 방향으로 바뀜
#     b_tmp = arr[f_idx]
#     f_count = 0
#     for i in range(b_idx, len(arr)):
#         if arr[i] > b_tmp:
#             f_count += 1
#         else:
#             break
#     result = min(b_count, f_count)
#     if f_count < b_count:
#         while f_count > 0:
#             arr[b_idx] = b_tmp
#             f_count -= 1
#             b_idx -= 1
#     else:
#         while b_count > 0:
#             arr[f_idx] = f_tmp
#             b_count -= 1
#             f_idx += 1
#     return result

