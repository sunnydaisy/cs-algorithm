

function solution(priorities, location) {
    let answer = 1;
    let prioritieAndIdx = priorities.map((pri, idx) => [pri, idx]);
    let maxPri = Math.max(...priorities);
    while (true) {
        let [pri, idx] = prioritieAndIdx.shift();
        if (pri === maxPri) {
            if (idx === location) return answer;
            priorities[idx] = -1;
            maxPri = Math.max(...priorities);
            answer++;
        } else {
            prioritieAndIdx.push([pri, idx])
        }
    }
    return answer;
}