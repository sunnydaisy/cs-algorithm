# 10872 팩토리얼
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num - 1)  
n = int(input())
print(factorial(n))

# 10870 피보나치수 5
def fibo(num):
    if num==0 or num==1:
        return num
    return fibo(num-2) + fibo(num-1) 
n = int(input())
print(fibo(n))

# 2447 별 찍기 - 10
import sys
sys.setrecursionlimit(10**6)
def star(n):
    if n==1:
        return ['*']
    stars = star(n//3)
    L = []
    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s+' '*(n//3)+s)
    for s in stars:
        L.append(s*3)
    return L
n = int(sys.stdin.readline().strip())
print('\n'.join(star(n)))

# 하노이
import sys
def hanoi(n, start, end):
    if n==1:
        print(start, end)
        return
    hanoi(n-1,start, 6-start-end)   # n-1개 원판을 1에서 3으로
    print(start, end)               # 마지막 원판을 1에서 3으로
    hanoi(n-1, 6-start-end, end)    # 2에 있는 n-1개 원판을 3으로
n = int(sys.stdin.readline().strip())
print(2**n-1) # 하노이 이동횟수 2^n -1
hanoi(n,1,3)