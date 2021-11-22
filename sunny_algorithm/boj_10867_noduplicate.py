# 백준 10867 중복빼고정렬하기
'''
정렬
N개의 정수를 오름차순으로 중복없이 정렬하는 프로그램
예제1
10
1 4 2 3 1 4 2 3 1 2
'''
import sys
num = int(input())
numlist = list(set(list(map(int,sys.stdin.readline().split()))))
numlist.sort()
for i in numlist:
    print(i, end=' ')
