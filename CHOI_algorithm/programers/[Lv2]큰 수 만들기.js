/**
 * 1차 시도
 * 정확성: 25.0
 * 합계: 25.0 / 100.0
 */
function combination(arr, selectNumber) {
    let result = [];

    if (selectNumber === 1) return arr.map(v => [v]);

    arr.forEach((fixed, idx, origin) => {
        const rest = origin.slice(idx + 1);
        const com = combination(rest, selectNumber - 1);
        const attached = com.map(v => [fixed, ...v]);
        result.push(...attached);
    })
    return result;
}

function getRemovedNum(str, numberIdx, idxs) {
    let result = "";
    numberIdx.forEach(v => {
        if (idxs.includes(v)) return;
        result += str[v];
    })
    return result;
}

function solution(number, k) {
    var answer = '';
    let numberIdx = number.split("").map((v, i) => i);
    let result = combination(numberIdx, k);
    result.forEach((idxs) => {
        let tmp = getRemovedNum(number, numberIdx, idxs);
        answer = "" + Math.max(+answer, +tmp);
    })

    return answer;
}