def solution(bridge_length, weight, truck_weights):
    next = truck_weights.pop(0)
    passing_list = []
    passing_list_weight = 0
    time = 0
    passed_list = []

    # 루프
    # 트럭 빼기
    while True:
        for truck in passing_list:
            if truck[1] == bridge_length:
                passed_list.append(truck[0])
                passing_list.pop(truck)
            else :
                # 모두 1시간 추가
                truck[1] += 1

        # 트럭 추가
        if weight >= passing_list_weight + next:
            passing_list.append((next, 0))

        if len(passed_list) == len(truck_weights):
            break
        time += 1
    return time


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))