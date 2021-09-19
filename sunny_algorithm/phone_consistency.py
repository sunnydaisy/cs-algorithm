# 백준 5052 전화번호목록
'''
정렬
전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 함 -> 일관성유지O 'YES', X 'NO'
예제1
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
'''
import sys
num = int(input())
phone = []
for i in range(num):
    cnt = int(input())
    phone = [sys.stdin.readline().split('\n')[0] for j in range(cnt)]
    phone.sort()
    result = 'YES'

    for i in range(len(phone)-1):
        if phone[i]==phone[i+1][:len(phone[i])]:
            result = 'NO'
            break
    print(result)
