# 성적이 낮은 순서로 학생 출력하기
n = int(input())
list = []
for _ in range(n):
    list.append(input().split())
list.sort(key=lambda x : x[1])

for name, score in list:
    print(name, end=' ')