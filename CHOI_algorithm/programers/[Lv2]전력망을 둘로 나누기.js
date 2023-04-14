/**
 * findParents 를 전부 초기화 해주는 작업이 필요했었음
 */

function findParents(parents, n) {
    if (parents[n] !== n) parents[n] = findParents(parents, parents[n]);
    return parents[n];
}

function unionParents(parents, a, b) {
    a = findParents(parents, a);
    b = findParents(parents, b);
    if (a < b) parents[b] = a;
    else parents[a] = b;
}

function getDiff(parents) {
    let count = 0;
    let target;
    parents.slice(1).forEach((v, i) => {
        if (i === 0) {
            target = findParents(parents, v); // 이부분
        }
        if (target === findParents(parents, v)) count++; // 이부분
        else count--;
    });
    return Math.abs(count);
}

function solution(n, wires) {
    var answer = 100;

    wires.forEach((removeTarget, removeIdx) => {
        let parents = new Array(n + 1).fill(0).map((_, i) => i);
        wires.forEach(([a, b], i) => {
            if (i !== removeIdx) {
                unionParents(parents, a, b);
            }
        });
        answer = Math.min(answer, getDiff(parents))
    })
    return answer;
}