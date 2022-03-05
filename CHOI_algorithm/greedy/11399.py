# t

n = int(input())
list = list(map(int, input().split()))

list.sort()
result = 0
tmp = 0

for i in list:
    result += tmp + i
    tmp += i

print(result)
