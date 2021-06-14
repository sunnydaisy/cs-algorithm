def solution(bridge_length, weight, truck_weights):
    time = 1
    passed_truck=[]
    passing_truck=[]
    truck_num = len(truck_weights)
    waiting_truck = truck_weights
    passing_weight = 0
    check_time = []


    #### 루프
    while len(passed_truck) != truck_num:
        # check_time 가 현재 시간일때
        if len(check_time) !=0 and time == check_time[0]:
            # 시간 체크 리스트에서 지우기
            check_time.remove(check_time[0])
            # 건넌 트럭 리스트에 추가
            passed_truck.append(passing_truck.pop(0))
            # 건너는중 무게에서 빼기
            passing_weight -= passed_truck[-1]



        # 건널 수 있으면
        if len(waiting_truck) !=0 and weight >= passing_weight + waiting_truck[0] and bridge_length >= len(passing_truck)+1:
            passing_weight += waiting_truck[0]
            passing_truck.append(waiting_truck.pop(0))
            check_time.append(time+bridge_length)
            time += 1
        elif len(waiting_truck)==0:
            return check_time[-1]
        else:
            time = check_time[0]

    return time