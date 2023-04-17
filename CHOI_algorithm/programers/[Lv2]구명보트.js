/**
 * 정확성: 75.0
 * 효율성: 0.0
 * 합계: 75.0 / 100.0
 */
function solution(people, limit) {
    var answer = 0;
    let done = [];
    people.sort((a, b) => b - a);
    let left = [...people];
    while (done.length !== people.length) {
        let botes = [];
        let big = left.shift();
        botes.push(big);
        let sum = big;
        while (true) {
            let tmp = left.pop();
            if (!tmp) break;
            if (tmp + sum > limit) {
                left.push(tmp);
                break;
            }
            sum += tmp;
            botes.push(tmp);
        }
        done = [...done, ...botes];
        botes
        answer++;
        // break;
        // if (answer === 3) break;
    }

    return answer;
}