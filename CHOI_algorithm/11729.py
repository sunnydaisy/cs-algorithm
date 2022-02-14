N = int(input())

t = N

def recursive(n, fr, tmp, to):
	global count
	count += 1
	if (n == 1):
		prt.append((fr[0], to[0]))
		to.append(fr.pop())
		return 
	else:
		recursive(n - 1, fr, to, tmp)
		to.append(fr.pop())
		prt.append((fr[0], to[0]))
		recursive(n - 1, tmp, fr, to)
	return

a = [1]
b = [2]
c = [3]
prt = []
count = 0
for i in range(t, 0, -1):
	a.append(i)
recursive(t, a, b, c)
print(count)
for a in prt:
	print(a[0], a[1])