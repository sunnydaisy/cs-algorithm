# 백준 11399 ATM
'''
정렬
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
예제1
5
3 1 4 3 2
'''
num = int(input())
numlist = sorted(list(map(int,input().split())))
sumlist = [sum(numlist[:i+1]) for i in range(num)]
print(sum(sumlist))
