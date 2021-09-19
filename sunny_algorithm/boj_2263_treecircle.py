# 백준 2263 트리의순회
'''
트리
이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램
예제1
3
1 2 3
1 3 2
'''
import sys
sys.setrecursionlimit(10 ** 6)

def solve(l_in, r_in, l_post, r_post):
    if l_in > r_in or l_post > r_post:
        return
    parent = postorder[r_post]
    print(parent, end=' ')

    s_idx = idx[parent]
    left = s_idx - l_in

    solve(l_in, s_idx-1, l_post, (l_post+left)-1) # left
    solve(s_idx+1, r_in, l_post+left, r_post-1) # right

num = int(input())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int,sys.stdin.readline().split()))

idx = [0] * (num+1)
for i in range(num):
    idx[inorder[i]]=i
solve(0, num-1, 0, num-1)