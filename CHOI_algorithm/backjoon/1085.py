def diff(a, b):
	if a > b:
		return a - b
	else:
		return b - a

x, y, w, h = map(int, input().split())

min = diff(x, w)
if min > diff(y, h):
	min = diff(y, h)
if min > diff(y, 0):
	min = diff(y, 0)
if min > diff(x, 0):
	min = diff(x, 0)

print(min)

