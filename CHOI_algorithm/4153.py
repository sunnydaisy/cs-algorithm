while (True):
	a,b,c = map(int, input().split())
	if a == 0 and b == 0 and c == 0:
		break
	l = [a, b, c]
	l.sort(reverse=True)
	if l[0]**2 == l[1]**2 + l[2]**2:
		print("right")
	else:
		print("wrong")
