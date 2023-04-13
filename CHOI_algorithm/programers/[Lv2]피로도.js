/**
 * 풀이 1. 순열
 */
function getTravelCount(k, arr) {
    let count = 0;
    arr.forEach(([min, cost]) => {
        if (k < min) return;
        k -= cost;
        count++;
    });
    return count;
}

function getPermutation(arr, selectNumber) {
    const result = [];

    if (selectNumber === 1) return arr.map(el => [el]);

    arr.forEach((fixed, idx, origin) => {
        const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
        const permutations = getPermutation(rest, selectNumber - 1);
        const attached = permutations.map(el => [fixed, ...el]);
        result.push(...attached);
    });
    return result;
}

function solution(k, dungeons) {
    var answer = -1;
    getPermutation(dungeons, dungeons.length)
        .forEach(order => {
            let result = getTravelCount(k, order);
            answer = Math.max(answer, result);
        })

    return answer;
}