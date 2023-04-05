

// 1tr tail
function getDeliverIdxs(cap, n, deliveries,) {
    let deliverIdxs = [];
    let deliverCount = 0;
    for (let i = deliveries.length - 1; i >= 0 ; i--) {
        if (deliveries[i] > 0) {
            let newDelCount = Math.min(deliveries[i], cap - deliverCount);
            console.log(`newDelCount ${newDelCount}`);
            deliverCount += newDelCount;
            deliverIdxs.push(i);
            if (deliverCount === cap) {
                break;
            }
        }
    }
    return deliverIdxs;
}

function solution(cap, n, deliveries, pickups) {
    // 최대한 멀리 있는 곳부터 배달한다.
    // cap 보다 적은양을 멀리 인 곳으로 배달해야 한다면 도중에 가는길에 제일 멀리있는 곳에 배달을 하고 간다.
    var answer = -1;

    let a = getDeliverIdxs(cap, n, deliveries);
    console.log(a);


    return answer;
}
