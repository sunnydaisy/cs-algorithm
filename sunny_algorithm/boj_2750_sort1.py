# O(n²)의 시간 복잡도 (버블정렬, 선택정렬, 삽입정렬)

# import sys
# # 버블정렬
# # 인접한 두 수를 비교하며 정렬, 앞에서부터 시작하여 큰 수를 뒤로 보내 뒤가 가장 큰 값을 가지도록 완성
def bubble(n):
    num = len(n)
    for i in range(num-1):
        for j in range(num-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
    print(n)

# # 선택정렬
# # 한 바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬.
def selection(n):
    num = len(n)
    for i in range(num):
        minidx = i
        for j in range(i+1,num):
            if n[minidx]>n[j]:
                minidx = j
        n[i], n[minidx] = n[minidx],n[i]
    print(n)

# # 삽입정렬
# # 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입하는 방식
def insert(n):
    num = len(n)
    for i in range(num):
        for j in range(i,0,-1):
            if n[j-1]>n[j]:
                n[j-1],n[j] = n[j],n[j-1]
    print(n)

num = int(sys.stdin.readline().strip())
n = [int(sys.stdin.readline().strip()) for i in range(num)]
bubble(n)
selection(n)
insert(n)

