# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 모두 1이 들어와 있는지 확인하는 함수
def answer_ck(sumed_lock):
    n = len(sumed_lock) // 3
    for i in range(n):
        for j in range(n):
            if sumed_lock[i + n][j + n] != 1:
                return False
    return True

def rotate_90_clock(graph):
    n = len(graph) # 행 길이
    m = len(graph[0]) # 열 길이
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = graph[i][j]
    return result

# 모든 경우의 수에 키를 넣는 함수
def sum_key_lock(key, new_lock):
    n = len(new_lock) - (len(new_lock) // 3)
    for _ in range(4):
        for i in range(1, n): 
            for j in range(1, n):
                # 키 넣기
                for q in range(len(key)):
                    for p in range(len(key)):
                        new_lock[i + q][j + p] += key[q][p]
                if (answer_ck(new_lock)):
                    return True
                # 다시 키 빼기
                for q in range(len(key)):
                    for p in range(len(key)):
                        new_lock[i + q][j + p] -= key[q][p]
        new_lock = rotate_90_clock(new_lock)
    return False


def solution(key, lock):
    n = len(lock)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)] # 3배 짜리 크기의 자물쇠 만들기
    # 가운데에 키 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    return (sum_key_lock(key, new_lock))

    

        

    
    


key = [[1, 0, 0], [1, 0, 1], [0, 0, 1]]	
lock = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]
rotate_90_clock(key)
print(solution(key, lock))