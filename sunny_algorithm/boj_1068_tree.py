# 백준 1068 트리
'''
트리
노드 하나를 지운 후 남은 트리 리프 노드의 개수를 구하는 프로그램
예제1
5
-1 0 0 1 1
2
예제2
5
-1 0 0 1 1
1
예제3
5
-1 0 0 1 1
0
예제4
9
-1 0 0 2 2 4 4 6 6
4
'''
import sys
class Tree:
    def createNode(self,data):
        self.left = None
        self.data = data
        self.right = None
    
num = int(input())
numlist = sys.stdin.readline().split()
tree = Tree()
for i in numlist:
    tree.createNode(i)
    