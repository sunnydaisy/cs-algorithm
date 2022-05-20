# 퇴사
# https://www.acmicpc.net/problem/14501


# ----------------------- 해설
def solution():
    n = int(input())
    dp = [0] * (n + 1)
    t_arr = []
    p_arr = []
    max_value = 0

    for i in range(n):
        t, p = map(int, input().split())
        t_arr.append(t)
        p_arr.append(p)

    for i in range(n-1, -1, -1):
        time = t_arr[i] + i
        # 상담이 기간 안에 끝나는 경우
        if time <= n:
            dp[i] = max(p_arr[i] + dp[time], max_value) # 자기 자신 + 자기 자신 끝난 뒤에 최대값(dp[time]) 이 큰지 아니면 지금까지의 있던 값들중의 최대가 큰지 비교
            max_value = dp[i]
        else:
            dp[i] = max_value
            
    print(max_value)


solution()