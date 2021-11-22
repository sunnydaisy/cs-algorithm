def is_prime(ck):
	if ck < 2:
		return (False)
	elif ck == 2 or ck == 3:
		return (True)
	else:
		i = 2
		while (i < ck):
			if ck % i == 0:
				return (False)
			i += 1
		return (True)

n = int(input())
answer = 0
ck = map(int, input().split())
for i in ck:
	if is_prime(i):
		answer += 1

print(answer)
