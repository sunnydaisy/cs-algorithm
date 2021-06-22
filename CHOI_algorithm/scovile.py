def solution(scoville, K):
    count = 0
    while len(scoville) > 1:
        if min(scoville) >= K:
            return count
        f_min_scoville = scoville.pop(scoville.index(min(scoville)))
        s_min_scoville = scoville.pop(scoville.index(min(scoville)))*2
        scoville.append(f_min_scoville+s_min_scoville)
        print(scoville)
        count += 1

    if scoville[0] >= K:
        return count

    return -1