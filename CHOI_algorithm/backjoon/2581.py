def is_prime(nb):
	if nb < 2:
		return (False)
	elif nb == 2 or nb == 3:
		return (True)
	else:
		i = 2
		while (i < nb):
			if nb % i == 0:
				return (False)
			i += 1
		return (True)


n1 = int(input())
n2 = int(input())

map = [i for i in range(n1, n2 + 1) if is_prime(i)]
if len(map) == 0:
	print(-1)
else:
	print(sum(map))
	print(min(map))

