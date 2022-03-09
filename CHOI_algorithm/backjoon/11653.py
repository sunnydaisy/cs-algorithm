"""
def is_prime(nb):
	if nb < 2:
		return (False)
	elif nb == 2 or nb == 3:
		return (True)
	elif nb % 2 == 0 or nb % 3 == 0:
		return (False)
	else:
		i = 2
		while (i <= nb**0.5 + 1):
			if nb % i == 0:
				return (False)
			i += 1
		return (True)
"""
n = int(input())
i = 2
while i <= n:
	if n % i == 0:
		print(i)
		n /= i
		continue
	i += 1

