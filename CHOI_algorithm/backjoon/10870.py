def fibonachi(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonachi(n - 2) + fibonachi(n - 1)

n = int(input())
print(fibonachi(n))
