import numpy as np


def solution(progresses, speeds):
    answer = []
    stop_indexs = []
    progresses_ar = np.array(progresses)
    speeds_ar = np.array(speeds)

    for i, v in enumerate(progresses_ar):
        if v < 100:
            stop_indexs.append(i)
            while progresses_ar[i] < 100:
                progresses_ar += speeds_ar

    for i in range(len(stop_indexs)):
        # 멈춘 인덱스중 마지막 빼고
        if i != len(stop_indexs)-1:
            answer.append(stop_indexs[i+1] - stop_indexs[i])
        # 멈춘 인덱스중 마지막 값
        else:
            last_answer = len(progresses)-1 - stop_indexs[i]
            if last_answer == 0:
                answer.append(1)
            else:
                answer.append(last_answer + 1)
    return answer






