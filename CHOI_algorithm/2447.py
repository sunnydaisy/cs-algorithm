def start(n):
	if n == 1:
		return ('*')
	elif n % 3 != 0:
		return (' ')
	print(start(n / 3),start(n / 3),start(n / 3))
	print(start(n / 3),start((n / 3) + 1),start(n / 3))
	print(start(n / 3),start(n / 3),start(n / 3))





N = int(input())
start(N)
