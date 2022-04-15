# 뱀
# https://www.acmicpc.net/problem/3190


from collections import deque

def turn_left(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction

def turn_right(direction):
    direction += 1
    if direction > 3:
        direction = 0
    return direction


def solution():
    n = int(input())
    graph = [[0]*n for _ in range(n)]

    dx = [-1, 0, 1, 0] # 북 ,동, 남, 서   행이동
    dy = [0, 1, 0, -1] # 북 ,동, 남, 서   열이동

    direction = 1 # 처음 시작은 동쪽으로
    time = 0 # 소모된 시간
    pos = [0, 0] # 현재 위치
    tmp_pos = [0, 0] # 이동할 위치

    k = int(input()) # 사과의 개수
    for _ in range(k):
        apple_point = list(map(int, input().split()))
        graph[apple_point[0] - 1][apple_point[1] - 1] = 1
    
    l = int(input()) # 방향 전환 정보 개수
    q = deque() # 큐
    q.append([0, 0])
    for _ in range(l):
        line = list(input().split())
        for i in line:
            if i.isdigit(): # 이동하기
                i = int(i)
                while (time < i):
                    time += 1 # 시간 증가
                    # 먼저 머리를 이동한다
                    pos[0] = pos[0] + dx[direction] # 행방향 이동
                    pos[1] = pos[1] + dy[direction] # 열방향 이동
                    
                    # 지도 밖인지 확인
                    if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
                        return time
                    
                    # 꼬리에 닿은 경우
                    if pos in q: 
                        return time

                    # 사과가 아닌 경우
                    if graph[pos[0]][pos[1]] != 1:
                        deque.popleft(q)
                    else:
                        graph[pos[0]][pos[1]] = 0

                    q.append(pos.copy()) # 머리를 큐에 삽입한다
            else : # 방향 바꾸기
                if i == "D":
                    direction =  turn_right(direction)# 오른쪽 방향
                elif i == "L":
                    direction =  turn_left(direction)# 왼쪽 방향
    
    # 방향 전환은 끝이고 벽에 닿을 떄 까지 계속 감
    while True:
        time += 1 # 시간 증가
        # 먼저 머리를 이동한다
        pos[0] = pos[0] + dx[direction] # 행방향 이동
        pos[1] = pos[1] + dy[direction] # 열방향 이동
        
        # 지도 밖인지 확인
        if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
            return time
        
        if pos in q: # 꼬리에 닿은 경우
            return time
        # 사과가 아닌 경우
        if graph[pos[0]][pos[1]] != 1:
            deque.popleft(q)
        else:
            graph[pos[0]][pos[1]] = 0

        q.append(pos.copy()) # 머리를 큐에 삽입한다.

print(solution())


# -----------------------------시도 1 : 이동한 칸에 사과가 있다면 이동 후 부터 길어진다는 것을 간과했다. 
# from collections import deque

# def turn_left(direction):
#     direction -= 1
#     if direction < 0:
#         direction = 3
#     return direction

# def turn_right(direction):
#     direction += 1
#     if direction > 3:
#         direction = 0
#     return direction


# def solution():
#     n = int(input())
#     graph = [[0]*n for _ in range(n)]

#     dx = [-1, 0, 1, 0] # 북 ,동, 남, 서   행이동
#     dy = [0, 1, 0, -1] # 북 ,동, 남, 서   열이동

#     direction = 1 # 처음 시작은 동쪽으로
#     time = 0 # 소모된 시간
#     pos = [0, 0] # 현재 위치
#     tmp_pos = [0, 0] # 이동할 위치

#     k = int(input()) # 사과의 개수
#     for _ in range(k):
#         apple_point = list(map(int, input().split()))
#         graph[apple_point[0] - 1][apple_point[1] - 1] = 1
    
#     l = int(input()) # 방향 전환 정보 개수
#     q = deque() # 큐
#     q.append([0, 0])
#     for _ in range(l):
#         line = list(input().split())
#         for i in line:
#             if i.isdigit(): # 이동하기
#                 i = int(i)
#                 while (time < i):
#                     time += 1 # 시간 증가
#                     tmp_pos[0] = pos[0] + dx[direction] # 행방향 이동
#                     tmp_pos[1] = pos[1] + dy[direction] # 열방향 이동
                    
#                     # 지도 밖인지 확인
#                     if tmp_pos[0] < 0 or tmp_pos[0] >= n or tmp_pos[1] < 0 or tmp_pos[1] >= n:
#                         return time
                    
#                     # 사과인 경우
#                     if graph[tmp_pos[0]][tmp_pos[1]] == 1:
#                         graph[tmp_pos[0]][tmp_pos[1]] = 0
#                         q.append(tmp_pos.copy())
#                     elif tmp_pos in q: # 꼬리에 닿은 경우
#                         return time
#                     else: # 그 외의 경우
#                         deque.popleft(q)
#                         q.append(tmp_pos.copy())
#                     pos[0] = tmp_pos[0] # 행방향 이동
#                     pos[1] = tmp_pos[1] # 열방향 이동
#             else : # 방향 바꾸기
#                 if i == "D":
#                     direction =  turn_right(direction)# 오른쪽 방향
#                 elif i == "L":
#                     direction =  turn_left(direction)# 왼쪽 방향
    
#     # 방향 전환은 끝이고 벽에 닿을 떄 까지 계속 감
#     while not (pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n):
#         time += 1
#         pos[0] = pos[0] + dx[direction] # 행방향 이동
#         pos[1] = pos[1] + dy[direction] # 열방향 이동
#         deque.popleft(q) # 꼬리 이동
#         if pos in q:
#             break
#         q.append(pos.copy()) # 머리 이동
#     return time 

# print(solution())