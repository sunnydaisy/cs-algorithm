when = int(input())

x, y = 1, 1
cnt = 1
while (cnt != when):
	if x == 1 and y % 2 != 0:
		y += 1
	elif y == 1 and x % 2 == 0:
		x += 1
	elif ((x + y) % 2) != 0:
		x += 1
		y -= 1
	elif ((x + y) % 2) == 0:
		x -= 1
		y += 1
	cnt += 1

print(x, '/', y, sep="")
