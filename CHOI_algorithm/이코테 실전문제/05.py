import time
# 볼링공 고르기

# 2회차

def tr1():
	n, m = map(int, input().split())
	balls = list(map(int, input().split()))
	result = 0
	pick = None
	for i in balls:
		for j in balls:
			if i == j:
				continue
			result += 1
	print(result // 2)


tr1()




# 해설 4.1초
# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# array = [0] * 11 
# for x in data:
# 	array[x] += 1
# result = 0
# for i in range(1, 1 + m):
# 	n -= array[i]
# 	result += array[i] * n



# 1회차

# # 내 답 5.5초
# n, m = map(int, input().split())
# ball_list = list(map(int, input().split()))

# ball_type = set(ball_list)
# result = 0
# for ball in ball_type:
# 	same_ct = ball_list.count(ball)
# 	big_ct = len([i for i in ball_list if i > ball])
# 	result += same_ct * big_ct


"""
testcase

5 3
1 3 2 3 2
answer : 8

8 5
1 5 4 3 2 4 5 2
asnwer : 25

"""