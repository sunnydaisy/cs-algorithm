a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


def solution(x):
	for i in x:
		if x.count(i) == 1 or x.count(i) == 3:
			return i


arr_x = [a[0], b[0], c[0]]
arr_y = [a[1], b[1], c[1]]

print(solution(arr_x), solution(arr_y))
