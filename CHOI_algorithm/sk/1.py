def solution(p):
    answer = [0] * len(p)
    # report = [0] * 1001

    tmp = p.copy()
    i = 0
    n = len(p)
    while i < n:
        pivot = [p[i], i]
        min_num = [int(1e9), -1]

        for j in range(i+1, n):
            if p[j] < min_num[0]:
                min_num = [p[j], j]

        if pivot[0] > min_num[0]:
            answer[pivot[1]] += 1
            answer[min_num[1]] += 1
            p[pivot[1]], p[min_num[1]] = p[min_num[1]], p[pivot[1]]
        i += 1


    return answer

p = [2, 5, 3, 1, 4]
solution(p)
