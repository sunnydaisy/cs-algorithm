# 2739 구구단
n = int(input())
for i in range(1,10):
    print('%d * %d = %d' %(n,i,n*i))

# 10950 A+B - 3
num = int(input())
for i in range(num):
    a,b = map(int,input().split())
    print(a+b)

# 8393 합
import sys
n = int(sys.stdin.readline().rstrip())
sum = 0
for i in range(1,n+1):
    sum+=i
print(sum)

# 15552 빠른 A+B
import sys
num = int(sys.stdin.readline())
for i in range(num):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(a+b)

# 2741 N찍기
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1,n+1):
    print(i)

# 2742 기찍N
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    print(n-i)

# 11021 A+B - 7
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1,n+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print('Case #%d: %d' %(i,a+b))

# 11022 A+B - 8
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1,n+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print('Case #%d: %d + %d = %d' %(i, a, b, a+b))

# 2439 별 찍기 - 1
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(1,n+1):
    print('*'*i)
    

# 2439 별 찍기 - 2
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print('')

# 10871 X보다 작은 수
import sys
n,x = map(int,sys.stdin.readline().rstrip().split())
num = list(map(int,sys.stdin.readline().rstrip().split()))
for i in num:
    if i < x:
        print(i, end=' ')