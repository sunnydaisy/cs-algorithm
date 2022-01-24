import sys

class Stack:
	def __init__(self, idx):
		self.items = []
		self.idx = idx
	def pop(self):
		return self.items.pop()
	def push(self, item):
		self.items.append(item)
	def peek(self):
		return self.items[-1]

def move(fr, to):
	to.push(fr.pop())
	print(fr.idx, to.idx)
	# print(a.items, b.items, c.items)

def a_to_c_321(frm, tmp, to):
	# print("@@@@@",frm.idx, to.idx)
	move(frm, to)
	move(frm, tmp)
	move(to, tmp)
	move(frm, to)
	move(tmp, frm)
	move(tmp, to)
	move(frm, to)

def solution(n, a, b, c):
	if n == 3:
		a_to_c_321(a, b, c)
		return
	solution(n-1, a, c, b)
	move(a, c)
	solution(n-1, b, a, c)

def count(n):
	if n == 3:
		return 7
	return count(n-1) * 2 + 1



g_n = int(input())
# g_n = 8
g_count = 0
a = Stack(1)
b = Stack(2)
c = Stack(3)
a.items = [i for i in range(g_n, 0, -1)]
print(count(g_n))
solution(g_n,a,b,c)

# move(a, c)
# move(b, c)
# move(b, a)
# move(c, a)
# move(b, c)
# move(a, b)
# move(a, c)
# move(b, c)

# move(a, c)
# move(a, b)
# move(c, b)
# move(a, c)
# move(b, a)
# move(b, c)
# move(a, c)
# #######
# move(a, b)
# move(c, b)
# move(c, a)
# move(b, a)
# move(c, b)
# move(a, c)
# move(a, b)
# move(c, b)
# move(a, c)
# ######3
# move(b ,a)
# move(b, c)
# move(a, c)
# move(b, a)
# move(c, b)
# move(c, a)
# move(b, a)
# move(b, c)
# #######
# move(a, c)
# move(a, b)
# move(c, b)
# move(a, c)
# move(b, a)
# move(b, c)
# move(a, c)

