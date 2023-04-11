// 2차 성공
function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let truckInfos = truck_weights.map(w => ({
        weight : w,
        time : 0,
        isMoving : false,
    }));
    let nextIdx = 0;

    while (true) {



        // 1. 다리 건내고 있는 애들 건너기
        truckInfos = truckInfos.map(info => {
            if (info.isMoving) info.time++
            if (info.time > bridge_length) info.isMoving = false;
            return info
        });

        // 2. 추가할 트럭 있으면 추가하기
        let movingTrucks = truckInfos.filter(info => info.isMoving);
        let nowWeigths = movingTrucks.length ? movingTrucks
            .reduce((acc, info) => acc + info.weight, 0) : 0;

        if (truckInfos[nextIdx] &&
            nowWeigths + truckInfos[nextIdx].weight <= weight) {
            // 트럭 추가
            truckInfos[nextIdx].isMoving = true;
            truckInfos[nextIdx].time++;
            nextIdx++;
        }

        // 2.5. 시간 증가
        answer++;


        // 3. 다 건넜는지 확인하기
        if (truckInfos.filter(info => info.time <= bridge_length).length === 0) return answer;
    }
    return answer;
}