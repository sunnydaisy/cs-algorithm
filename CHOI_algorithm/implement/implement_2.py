# 문자열 재정렬

def solution():
    alpha = [0] * 26
    result_num = 0
    s = input()
    for i in s:
        tmp = ord(i)
        if 48 <= tmp and tmp <= 57:
            result_num += int(i)
        else:
            alpha[tmp - ord("A")] += 1
    for i in range(len(alpha)):
        if alpha[i] != 0:
            print(chr(i + ord("A")) * alpha[i], end='')
    print(result_num)



solution()