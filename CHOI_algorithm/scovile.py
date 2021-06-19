def solution(scoville, K):
    count = 0
    while len(scoville) > 1:
        scoville.sort(reverse=True)
        if scoville[-1] >=K:
            return count
        new_food = scoville[-1] + scoville[-2] * 2
        scoville = scoville[:-2]
        scoville.append(new_food)
        count += 1
    if scoville[0] >= K:
        return count

    return -1
